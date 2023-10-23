/**
 * Static program definitions
 */
import { provide, inject, useRouter, computed } from "#imports";
import type { InjectionKey, Ref } from "@vue/runtime-core";
import type { Router } from "vue-router";

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

type EncodedUrlState = ([string, ProgramVisibility, string] | [string, ProgramVisibility])[];

export class ProgramManager {
    private router: Router;

    constructor() {
        this.router = useRouter();
    }

    /**
     * Deserialize current program state from URL
     */
    private deserializeState(): Ref<Map<string, [ProgramVisibility, string | null]> | null> {
        return computed(() => {
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
                const state = (JSON.parse(serializedProgramStates) as EncodedUrlState)
                    // map triple into two tuples so that the map works
                    .map((entry) => {
                        if (entry.length == 2) return [entry[0], [entry[1], null]];
                        else return [entry[0], [entry[1], entry[2]]];
                    });
                // @ts-ignore
                return new Map(state);
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
        });
    }

    /**
     * Serialize the given program state and save it in the URL
     */
    private serializeState(state: Map<string, [ProgramVisibility, string | null]>): Promise<unknown> {
        const encodedState: EncodedUrlState = Array.from(state.entries())
            // remove programs that are closed because closed is also the default when a programId is not serialized at all
            .filter((i) => i[1][0] != "closed")
            // pull down (visibility, extra-data) tuple into the same level as the program id
            .map(([programId, [visibility, extraData]]) => {
                if (extraData == null) return [programId, visibility];
                else return [programId, visibility, extraData];
            });

        // serialize query and save it back to url
        const query = this.router.currentRoute.value.query;
        if (encodedState.length > 0) {
            query["programs"] = JSON.stringify(encodedState);
        } else {
            delete query["programs"];
        }
        return this.router.push({ query, force: true });
    }

    /**
     * Reorder the given state map to have the given program first.
     * Returns a new state map.
     */
    private reorderState<T>(state: Map<string, T>, topProgram: string): Map<string, T> {
        return new Map(
            [...state.entries()].sort((a, b) => {
                if (a[0] === topProgram) {
                    return -1;
                } else if (b[0] === topProgram) {
                    return 1;
                } else {
                    return 0;
                }
            })
        );
    }

    /**
     * Set the visibility state of the given program.
     * Optionally, the program can also be hoisted to the top of the program stack (useful when initially opening programs).
     */
    public setProgramVisibility(programId: string, visibility: ProgramVisibility): Promise<unknown>;
    public setProgramVisibility(
        programId: string,
        visibility: ProgramVisibility,
        raiseToTop: boolean
    ): Promise<unknown>;
    public setProgramVisibility(
        programId: string,
        visibility: ProgramVisibility,
        raiseToTop?: boolean
    ): Promise<unknown> {
        if (visibility === this.getProgramVisibility(programId).value) {
            return Promise.resolve();
        }

        let state = this.deserializeState().value || new Map();
        const [_, extraData] = state.get(programId) ?? ["", null];
        state.set(programId, [visibility, extraData]);

        if (raiseToTop != null && raiseToTop) {
            state = this.reorderState(state, programId);
        }
        return this.serializeState(state);
    }

    /**
     * Get the visibility of the given program
     */
    public getProgramVisibility(programId: string): Ref<ProgramVisibility> {
        const state = this.deserializeState();
        return computed(() => {
            if (state.value == null) return "closed";
            if (state.value!.get(programId) == null) return "closed";

            // return saved program state
            return state.value!.get(programId)!.at(0) as ProgramVisibility;
        });
    }

    public raiseWindow(programId: string): Promise<unknown> {
        const state = this.deserializeState().value;
        if (state == null || !state.has(programId)) {
            return Promise.resolve();
        }

        return this.serializeState(this.reorderState(state, programId));
    }

    /**
     * Get the position of the program in the stack of open programs.
     * 0 means the given program is on top.
     */
    public getStackPosition(programId: string): Ref<number | undefined> {
        const state = this.deserializeState();
        return computed(() => {
            if (state.value == null) {
                return undefined;
            }

            return [...state.value?.keys()].findIndex((key) => key === programId);
        });
    }

    public getExtraData(programId: string): Ref<string | null> {
        const state = this.deserializeState();
        return computed(() => {
            return state.value?.get(programId)?.at(1) || null;
        });
    }

    public setExtraData(programId: string, data: string | null) {
        let state = this.deserializeState().value;
        if (state == null || !state.has(programId)) {
            return Promise.resolve();
        }

        const [visibility, _] = state.get(programId)!;
        state.set(programId, [visibility, data]);
        return this.serializeState(state);
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
