/** @type {import('tailwindcss').Config} */
module.exports = {
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
            blue_of_death: "rgb(19, 0, 164)",
            titlebar_gradient: "linear-gradient(to right, #00007b 0%, #0884ce 100%)",
            shadow: {
                normal: "rgb(89, 89, 89)",
                inverse: "rgb(216, 216, 216)",
            },
        },
    },
    plugins: [],
};
