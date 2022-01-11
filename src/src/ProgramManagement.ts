import type { Readable } from "svelte/store";
import { derived } from "svelte/store";
import { page } from "$app/stores";
import { getContext } from "svelte";
import { goto } from "$app/navigation";

/**
 * Static program definitions
 */
export interface ProgramMetadata {
	/**
	 * String displayed in the program windows titlebar as well as the taskbar
	 */
	title: string;
	/**
	 * Internal program identifier
	 */
	programId: string;
	/**
	 * {@link https://materialdesignicons.com/|Mateial Design Icon} used for this program
	 */
	icon: string;
	/**
	 * TODO
	 */
	canOpen: boolean;
	/**
	 * Defaults used when rendering the program on the viewport
	 */
	renderDefaults: ProgramPlacement;
}

/**
 * Possible visibility variants which a program can be in
 */
export enum ProgramVisibility {
	CLOSED = "closed",
	OPENED = "opened",
	MINIMIZED = "minimized",
	MAXIMIZED = "maximized",
}

export interface ProgramPlacement {
	/**
	 * CSS value that will be used for the programs preferred horizontal offset
	 */
	x: string;
	/**
	 * CSS value that will be used for the programs preferred vertical offset
	 */
	y: string;
	/**
	 * CSS value that will be used for the programs preferred width
	 */
	width: string;
	/**
	 * CSS value that will be used for the programs preferred height
	 */
	height: string;
}

export interface ProgramState {
	programId: string;
	visibility: ProgramVisibility;
	isOnTop: boolean;
	placement: ProgramPlacement;
	programIndex: number | null;
}

/**
 * Svelte context name from which metadata of all known programs can be retrieved
 */
export const CTX_PROGRAM_METADATAS = "ProgramMetadataDefinitions";

/**
 * The visibility of the given program parsed from the current pages url
 *
 * The visibility is directly extracted from the given url.
 * Otherwise, a readable store is returned which will always produce the visibility based on the current url.
 */
function programVisibility(programId: string, url: URL): ProgramVisibility {
	return url.searchParams.has(programId)
		? (url.searchParams.get(programId) as ProgramVisibility)
		: ProgramVisibility.CLOSED;
}

/**
 * The window hierarchy index of the given program parsed from the current pages url
 *
 * If an url is given, the program index is directly extracted from it.
 * Otherwise, a readable store is returned which will always produce the program index based on the current url.
 */
function programIndex(programId: string, url: URL): number | null {
	return url.searchParams.has(`${programId}i`) ? parseInt(url.searchParams.get(`${programId}i`)) : null;
}

/**
 * Parameters used for rendering placement of the given program.
 */
function programPlacement(programId: string, url: URL, metadata: ProgramMetadata): ProgramPlacement {
	return {
		x: url.searchParams.has(`${metadata.programId}x`)
			? url.searchParams.get(`${metadata.programId}x`)
			: metadata.renderDefaults.x,
		y: url.searchParams.has(`${metadata.programId}y`)
			? url.searchParams.get(`${metadata.programId}y`)
			: metadata.renderDefaults.y,
		width: url.searchParams.has(`${metadata.programId}w`)
			? url.searchParams.get(`${metadata.programId}w`)
			: metadata.renderDefaults.width,
		height: url.searchParams.has(`${metadata.programId}h`)
			? url.searchParams.get(`${metadata.programId}h`)
			: metadata.renderDefaults.height,
	};
}

/**
 * The program which is currently on top of the window stack (or null if no program is open)
 */
function programOnTop(url: URL, allMetadata: ProgramMetadata[]): string | null {
	let resultI = null;
	let resultProgram = null;

	for (const metadata of allMetadata) {
		// getting the current value is fine because `programIndex` also only depends on the current page
		const i = programIndex(metadata.programId, url);
		if (i != null && (resultI == null || i < resultI)) {
			resultI = i;
			resultProgram = metadata.programId;
		}
	}

	return resultProgram;
}

/**
 * A store which produces the current state of the given program
 */
export function programState(programId: string): Readable<ProgramState> {
	const allMetadata = getContext<ProgramMetadata[]>(CTX_PROGRAM_METADATAS);
	const metadata = allMetadata.find((m) => m.programId === programId);

	return derived(page, ($page) => {
		return {
			programId: programId,
			visibility: programVisibility(programId, $page.url),
			placement: programPlacement(programId, $page.url, metadata),
			isOnTop: programOnTop($page.url, allMetadata) === programId,
			programIndex: programIndex(programId, $page.url),
		};
	});
}

/**
 * Object which can be used from components to manage programs
 */
export class ProgramManager {
	private allMetadata: ProgramMetadata[];
	private currentUrl: URL;

	/**
	 * Create a new ProgramManager instance.
	 *
	 * Must be called during component initiation and not later
	 */
	constructor() {
		this.allMetadata = getContext<ProgramMetadata[]>(CTX_PROGRAM_METADATAS);
		page.subscribe(($page) => (this.currentUrl = $page.url));
	}

	private normalizeUrl(url: URL): void {
		// normalize program indices
		// 	this works by sorting the non-closed program indices and then reassigning them in sorted order
		this.allMetadata
			.filter((metadata) => programVisibility(metadata.programId, url) !== ProgramVisibility.CLOSED)
			.sort((ma, mb) => programIndex(ma.programId, url) - programIndex(mb.programId, url))
			.forEach((metadata, i) => {
				url.searchParams.set(`${metadata.programId}i`, (i + 1).toString());
			});

		// remove search parameters of programs that are not open
		this.allMetadata
			.filter((metadata) => programVisibility(metadata.programId, url) === ProgramVisibility.CLOSED)
			.forEach((metadata) => {
				url.searchParams.delete(`${metadata.programId}i`);
				url.searchParams.delete(`${metadata.programId}x`);
				url.searchParams.delete(`${metadata.programId}y`);
				url.searchParams.delete(`${metadata.programId}w`);
				url.searchParams.delete(`${metadata.programId}h`);
			});
	}

	/**
	 * Raise the window of the specified program so that it is on top of the window stack.
	 */
	public raiseWindow(programId: string): Promise<unknown> {
		if (programVisibility(programId, this.currentUrl) === ProgramVisibility.CLOSED) {
			return Promise.resolve();
		}

		const newUrl = new URL(this.currentUrl);
		newUrl.searchParams.set(`${programId}i`, "0");
		this.normalizeUrl(newUrl);
		return goto(newUrl.href);
	}

	/**
	 * Set the visibility of the specified program to the specified value.
	 */
	public setProgramVisibility(programId: string, visibility: ProgramVisibility): Promise<unknown> {
		const newUrl = new URL(this.currentUrl);

		if (visibility !== ProgramVisibility.CLOSED) {
			newUrl.searchParams.set(programId, visibility);
		} else {
			newUrl.searchParams.delete(programId);
		}

		this.normalizeUrl(newUrl);
		return goto(newUrl.href);
	}

	public toggleProgramMinimization(programId: string): Promise<unknown> {
		if (programVisibility(programId, this.currentUrl) === ProgramVisibility.OPENED) {
			return this.setProgramVisibility(programId, ProgramVisibility.MINIMIZED);
		} else if (programVisibility(programId, this.currentUrl) === ProgramVisibility.MINIMIZED) {
			return this.setProgramVisibility(programId, ProgramVisibility.OPENED);
		}
	}

	public toggleProgramMaximization(programId: string): Promise<unknown> {
		if (programVisibility(programId, this.currentUrl) === ProgramVisibility.OPENED) {
			return this.setProgramVisibility(programId, ProgramVisibility.MAXIMIZED);
		} else if (programVisibility(programId, this.currentUrl) === ProgramVisibility.MAXIMIZED) {
			return this.setProgramVisibility(programId, ProgramVisibility.OPENED);
		}
	}
}
