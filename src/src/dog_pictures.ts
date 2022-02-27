import { Readable, readable } from "svelte/store";

const API_URL = "https://api.thedogapi.com/v1";
const API_KEY = "80ddd2c5-96d1-4b2e-bfb4-5a923e69800d";

// How a dog is modelled in the dog api
export interface ApiDog {
	id: string;
	url: string;
	width: number;
	height: number;
}

export const randomDogPicture: Readable<ApiDog> = readable(null, (set) => {
	fetch(`${API_URL}/images/search?limit=1&order=RANDOM`, {
		redirect: "manual",
		headers: {
			"x-api-key": API_KEY,
		},
	})
		.then((response) => response.json())
		.then((response) => {
			set(response[0] as ApiDog);
		})
		.catch(console.error);
});
