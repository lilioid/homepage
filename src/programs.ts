import { ProgramMetadata } from "~/composables/programManagement";
import { mdiAccount, mdiFireAlert, mdiGavel } from "@mdi/js";

export const cvMetadata: ProgramMetadata = {
    title: "CV",
    programId: "cv",
    canOpen: true,
    icon: mdiAccount,
    renderDefaults: {
        x: "50px",
        y: "30px",
        width: "min(80vw, 1200px)",
        height: "80vh",
    },
};

export const rickRollMetadata: ProgramMetadata = {
    title: "Finndows Defender",
    programId: "defender",
    icon: mdiFireAlert,
    canOpen: true,
    renderDefaults: {
        x: "20vw",
        y: "8vh",
        width: "900px",
        height: "700px",
    },
};

export const imprintMetadata: ProgramMetadata = {
    title: "Imprint",
    programId: "imprint",
    canOpen: true,
    icon: mdiGavel,
    renderDefaults: {
        x: "60vw",
        y: "55vh",
        width: "450px",
        height: "300px",
    },
};
