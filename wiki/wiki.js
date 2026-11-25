(function () {
    "use strict";

    const menu = document.getElementById("menuToggle");
    const nav = document.getElementById("mainNav");
    if (menu && nav) {
        const closeMenu = () => {
            nav.classList.remove("menu-open");
            menu.setAttribute("aria-expanded", "false");
        };
        menu.addEventListener("click", () => {
            const open = nav.classList.toggle("menu-open");
            menu.setAttribute("aria-expanded", String(open));
        });
        nav.querySelectorAll("a").forEach(link => link.addEventListener("click", closeMenu));
        document.addEventListener("click", event => {
            if (!event.target.closest("header")) closeMenu();
        });
        document.addEventListener("keydown", event => {
            if (event.key === "Escape" && nav.classList.contains("menu-open")) {
                closeMenu();
                menu.focus();
            }
        });
        window.matchMedia("(min-width: 701px)").addEventListener("change", closeMenu);
    }

    const form = document.getElementById("wiki-search-form");
    const input = document.getElementById("wiki-search-input");
    const results = document.getElementById("search-results");
    const announcement = document.getElementById("search-announcement");
    const entries = Array.isArray(window.MMORP_SEARCH) ? window.MMORP_SEARCH : [];
    let currentMatches = [];

    const normalize = value => value.toLocaleLowerCase().normalize("NFKD").replace(/[\u0300-\u036f]/g, "");
    function findMatches(query) {
        const terms = normalize(query).trim().split(/\s+/).filter(Boolean);
        if (!terms.length) return [];
        return entries.map(entry => {
            const title = normalize(entry.title);
            const haystack = normalize([entry.title, entry.category, entry.summary, entry.keywords].join(" "));
            if (!terms.every(term => haystack.includes(term))) return null;
            const fullQuery = terms.join(" ");
            const score = title === fullQuery ? 3 : title.startsWith(fullQuery) ? 2 : title.includes(fullQuery) ? 1 : 0;
            return {entry, score};
        }).filter(Boolean).sort((a, b) => b.score - a.score || a.entry.title.localeCompare(b.entry.title)).slice(0, 8).map(match => match.entry);
    }
    function closeResults() {
        results.hidden = true;
    }
    function updateResults() {
        const query = input.value.trim();
        results.replaceChildren();
        if (!query) {
            currentMatches = [];
            closeResults();
            announcement.textContent = "";
            return;
        }
        currentMatches = findMatches(query);
        if (currentMatches.length) {
            currentMatches.forEach(entry => {
                const link = document.createElement("a");
                const title = document.createElement("strong");
                const category = document.createElement("small");
                link.href = entry.slug + ".html";
                title.textContent = entry.title;
                category.textContent = entry.category + " · " + entry.summary;
                link.append(title, category);
                results.append(link);
            });
            announcement.textContent = currentMatches.length + (currentMatches.length === 1 ? " result" : " results") + " shown.";
        } else {
            const message = document.createElement("p");
            message.textContent = "No articles found. Try another name or keyword.";
            results.append(message);
            announcement.textContent = "No articles found.";
        }
        results.hidden = false;
    }
    if (form && input && results) {
        input.addEventListener("input", updateResults);
        input.addEventListener("focus", () => { if (input.value.trim()) updateResults(); });
        form.addEventListener("submit", event => {
            const query = input.value.trim();
            if (!query) return;
            event.preventDefault();
            updateResults();
            if (currentMatches.length) window.location.href = currentMatches[0].slug + ".html";
        });
        input.addEventListener("keydown", event => {
            if (event.key === "Escape") {
                closeResults();
                input.blur();
            } else if (event.key === "ArrowDown" && !results.hidden) {
                const first = results.querySelector("a");
                if (first) { event.preventDefault(); first.focus(); }
            }
        });
        results.addEventListener("keydown", event => {
            if (event.key === "Escape") { input.focus(); closeResults(); }
        });
        document.addEventListener("click", event => {
            if (!event.target.closest(".wiki-search")) closeResults();
        });
    }

    const filterBar = document.querySelector(".filter-bar");
    if (filterBar) {
        const buttons = Array.from(filterBar.querySelectorAll("button[data-filter]"));
        const groups = Array.from(document.querySelectorAll(".browse-group"));
        const status = document.getElementById("filter-announcement");
        function setFilter(filter, shouldAnnounce) {
            buttons.forEach(button => button.setAttribute("aria-pressed", String(button.dataset.filter === filter)));
            groups.forEach(group => { group.hidden = filter !== "all" && group.dataset.group !== filter; });
            if (shouldAnnounce) {
                const active = buttons.find(button => button.dataset.filter === filter);
                status.textContent = active ? active.textContent + " displayed." : "";
            }
        }
        filterBar.hidden = false;
        buttons.forEach(button => button.addEventListener("click", () => setFilter(button.dataset.filter, true)));
        document.addEventListener("click", event => {
            const link = event.target.closest("a[href]");
            if (!link) return;
            const destination = new URL(link.href, window.location.href);
            if (destination.pathname !== window.location.pathname || !destination.hash) return;
            const target = document.getElementById(decodeURIComponent(destination.hash.slice(1)));
            if (target && target.classList.contains("browse-group") && target.hidden) setFilter("all", false);
        });
        window.addEventListener("hashchange", () => {
            const target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
            if (target && target.classList.contains("browse-group") && target.hidden) {
                setFilter("all", false);
                target.scrollIntoView();
            }
        });
    }
}());
