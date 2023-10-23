import type { ProgramMetadata } from "#imports";
import {
    mdiAccount,
    mdiCodeBraces,
    mdiEmail,
    mdiFireAlert,
    mdiGavel,
    mdiMicrosoftWindowsClassic,
} from "@mdi/js";

export const startMenuMetadata: ProgramMetadata = {
    title: "Start",
    programId: "start",
    icon: mdiMicrosoftWindowsClassic,
    canOpen: true,
    taskbarSize: "small",
    renderDefaults: {
        x: "0",
        y: "calc(100vh - 600px - 55px)",
        width: "428px",
        height: "600px",
    },
};

export const cvMetadata: ProgramMetadata = {
    title: "CV",
    programId: "cv",
    canOpen: true,
    icon: mdiAccount,
    taskbarSize: "normal",
    renderDefaults: {
        x: "50px",
        y: "30px",
        width: "min(80vw, 1100px)",
        height: "80vh",
    },
};

export const contactMetadata: ProgramMetadata = {
    title: "Contact",
    programId: "contact",
    canOpen: true,
    icon: mdiEmail,
    taskbarSize: "normal",
    renderDefaults: {
        x: "70vw",
        y: "12vh",
        width: "600px",
        height: "fit-content",
    },
};

export const codingMetadata: ProgramMetadata = {
    title: "Coding",
    programId: "coding",
    icon: mdiCodeBraces,
    canOpen: true,
    taskbarSize: "normal",
    renderDefaults: {
        x: "16vw",
        y: "1vh",
        width: "45vw",
        height: "88vh",
    },
};

export const rickRollMetadata: ProgramMetadata = {
    title: "Finndows Defender",
    programId: "defender",
    icon: mdiFireAlert,
    canOpen: true,
    taskbarSize: "normal",
    renderDefaults: {
        x: "20vw",
        y: "12vh",
        width: "fit-content",
        height: "fit-content",
    },
};

export const imprintMetadata: ProgramMetadata = {
    title: "Imprint",
    programId: "imprint",
    canOpen: true,
    icon: mdiGavel,
    taskbarSize: "normal",
    renderDefaults: {
        x: "62vw",
        y: "47vh",
        width: "450px",
        height: "fit-content",
    },
};
