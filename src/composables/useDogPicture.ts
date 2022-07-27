const API_URL = "https://api.thedogapi.com/v1";
const API_KEY = "80ddd2c5-96d1-4b2e-bfb4-5a923e69800d";

export interface RemoteDog {
    id: string;
    url: string;
    width: number;
    height: number;
}

export async function useDogPicture(): Promise<RemoteDog> {
    return $fetch<RemoteDog[]>(`${API_URL}/images/search?limit=1&order=RANDOM`, {
        headers: {
            "x-api-key": API_KEY,
        },
    }).then((response) => response[0]);
}
