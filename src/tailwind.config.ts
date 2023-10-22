import type { Config } from "tailwindcss";

export default <Partial<Config>>{
    content: [],
    theme: {
        fontFamily: {
            sans: ['"Source Sans Pro"', '"sans-serif"'],
            serif: ['"Source Serif Pro"', '"serif"'],
            mono: ['"Cutive Mono", "monospace"'],
        },
        colors: {
            transparent: "transparent",
            cyan: "rgb(0, 123, 123)",
            white: "rgb(255, 255, 255)",
            black: "rgb(0, 0, 0)",
            grey: {
                normal: "rgb(189, 189, 189)",
                light: "rgb(240, 240, 240)",
                dark1: "rgb(138, 138, 138)",
                dark2: "rgb(62, 62, 62)",
            },
            link_blue: "rgb(19,0,240)",
            blue_of_death: "rgb(19, 0, 164)",
        },
        borderColor: {
            "shadow-inverse": "#595959 #d9d9d9 #d9d9d9 #595959",
            shadow: "#d9d9d9 #595959 #595959 #d9d9d9",
            grey: "rgb(189, 189, 189)",
        },
    },
    plugins: [],
};
