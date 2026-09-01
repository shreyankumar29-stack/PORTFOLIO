/* =========================================================
   THEME TOGGLE
   ========================================================= */

const themeToggle = document.getElementById("theme-toggle");

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {

    document.body.classList.add("dark-mode");

    themeToggle.textContent = "☀️";

} else {

    themeToggle.textContent = "🌙";

}


/* =========================================================
   DARK / LIGHT MODE
   ========================================================= */

themeToggle.addEventListener("click", () => {

    document.body.classList.toggle("dark-mode");

    const isDark =
        document.body.classList.contains("dark-mode");


    if (isDark) {

        localStorage.setItem("theme", "dark");

        themeToggle.textContent = "☀️";

    } else {

        localStorage.setItem("theme", "light");

        themeToggle.textContent = "🌙";

    }

});


/* =========================================================
   PAGE TRANSITION
   ========================================================= */

document.addEventListener("DOMContentLoaded", () => {

    const links = document.querySelectorAll(
        "a[href]"
    );


    links.forEach((link) => {

        link.addEventListener("click", (event) => {

            const href = link.getAttribute("href");


            /*
             * Ignore:
             * - external links
             * - GitHub
             * - LinkedIn
             * - email links
             * - telephone links
             * - new-tab links
             * - same-page anchors
             */

            if (
                !href ||
                href.startsWith("http") ||
                href.startsWith("mailto:") ||
                href.startsWith("tel:") ||
                href.startsWith("#") ||
                link.target === "_blank"
            ) {
                return;
            }


            event.preventDefault();


            document.body.classList.add(
                "page-exit"
            );


            setTimeout(() => {

                window.location.href = href;

            }, 250);

        });

    });

});