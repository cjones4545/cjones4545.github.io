const themeToggle = document.getElementById("theme-toggle");
const themeIcon = themeToggle.querySelector(".theme-icon");
const themeLabel = themeToggle.querySelector(".theme-label");

function applyTheme(theme) {
    const isDark = theme === "dark";

    document.documentElement.dataset.theme = theme;

    themeToggle.setAttribute("aria-pressed", String(isDark));
    themeToggle.setAttribute(
        "aria-label",
        isDark ? "Switch to light mode" : "Switch to dark mode"
    );

    themeIcon.textContent = isDark ? "☀" : "☾";
    themeLabel.textContent = isDark ? "Light" : "Dark";
}

const currentTheme =
    document.documentElement.dataset.theme || "light";

applyTheme(currentTheme);

themeToggle.addEventListener("click", () => {
    const activeTheme =
        document.documentElement.dataset.theme || "light";

    const nextTheme =
        activeTheme === "dark" ? "light" : "dark";

    applyTheme(nextTheme);

    localStorage.setItem("portfolio-theme", nextTheme);
});