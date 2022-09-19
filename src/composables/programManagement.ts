/**
 * Static program definitions
 */
import { provide, inject, useRouter } from "#imports";
import { InjectionKey, Ref } from "@vue/runtime-core";
import { Router } from "vue-router";

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
    /**
     * How large the programs taskbar button is rendered
     */
    taskbarSize: "small" | "normal";
}

/**
 * Information about how a program is rendered where
 */
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

export type ProgramVisibility = "closed" | "opened" | "minimized" | "maximized";

export class ProgramManager {
    private router: Router;

    constructor() {
        this.router = useRouter();
    }

    /**
     * Deserialize current program state from URL
     */
    private deserializeState(): Record<string, ProgramVisibility | undefined> | null {
        // get the correct url parameter (or the first values if multiple are specified)
        const serializedProgramStates =
            this.router.currentRoute.value.query["programs"] instanceof Array
                ? this.router.currentRoute.value.query["programs"][0]
                : this.router.currentRoute.value.query["programs"];

        // return early if the parameter is empty
        if (serializedProgramStates == null) {
            return null;
        }

        // try to parse program states from url parameter
        try {
            return JSON.parse(serializedProgramStates);
        } catch (e) {
            console.warn("Could not deserialize programStates from url parameter. Clearing it.", e);
            let query = this.router.currentRoute.value.query;
            delete query["programs"];
            this.router
                .replace({
                    query,
                    force: true,
                })
                .then();
            return null;
        }
    }

    /**
     * Serialize the given program state and save it in the URL
     */
    private serializeState(state: Record<string, ProgramVisibility | undefined>): Promise<unknown> {
        // normalize state to remove all "closed" markers because that is the default when a marker is missing
        for (const programId of Object.keys(state)) {
            if (state[programId] === "closed") {
                delete state[programId];
            }
        }

        // serialize query and save it back to url
        const query = this.router.currentRoute.value.query;
        if (Object.keys(state).length > 0) {
            query["programs"] = JSON.stringify(state);
        } else {
            delete query["programs"];
        }
        return this.router.push({ query, force: true });
    }

    /**
     * Set the visibility state of the given program
     */
    public setProgramVisibility(programId: string, visibility: ProgramVisibility): Promise<unknown> {
        console.debug(`setting ${programId} to ${visibility}`);
        if (visibility === this.getProgramVisibility(programId)) {
            return Promise.resolve();
        }

        let state = this.deserializeState() || {};
        state[programId] = visibility;
        return this.serializeState(state);
    }

    /**
     * Get the visibility of the given program
     */
    public getProgramVisibility(programId: string): ProgramVisibility {
        // return saved program state
        return this.deserializeState()?.[programId] || "closed";
    }

    public raiseWindow(programId: string): Promise<unknown> {
        throw Error("not yet implemented");
    }
}

const programManagerKey: InjectionKey<ProgramManager> = Symbol("ProgramManager");

export function useProgramManager(): ProgramManager {
    const result = inject(programManagerKey);
    if (result == undefined) {
        throw Error(
            "No programManager has been provided. Ensure to call provideProgramManager() in your component hierarchy"
        );
    }
    return result;
}

export function provideProgramManager(): void {
    provide(programManagerKey, new ProgramManager());
}
