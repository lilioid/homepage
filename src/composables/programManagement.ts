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
