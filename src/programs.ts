import { ProgramMetadata } from "~/composables/programManagement";
import { mdiAccount } from "@mdi/js";

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
