// small script for color schem that is inlined to prevent brief screen flashes on load
(() => {
    const MEDIA_QUERY = window.matchMedia("(prefers-color-scheme: light)");

    function toggleTheme() {
        let new_theme = localStorage.color_theme === "light" ? "dark" : (localStorage.color_theme === "dark" ? "light" : undefined);
        if (new_theme === undefined) {
            new_theme = MEDIA_QUERY.matches ? "dark" : "light";
        }

        localStorage.color_theme = new_theme;
        applyTheme()
    }

    function applyTheme() {
        if (localStorage.color_theme != null) {
            document.documentElement.dataset.theme = localStorage.color_theme;
        } else {
            document.documentElement.dataset.theme = MEDIA_QUERY.matches ? "light" : "dark";
        }
    }

    MEDIA_QUERY.addEventListener("change", applyTheme)
    applyTheme();
    document.getElementById("theme-toggle").addEventListener("click", toggleTheme)
})();
