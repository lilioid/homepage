/// <reference types="@sveltejs/kit" />

interface Dictionary<T> {
	[Key: string]: T;
}
