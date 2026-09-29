/* The renders share a camera and canvas size. Leave them uncropped.
   0 = concept, 100 = PETG, 200 = PC-CF. Fade only the next layer over
   an opaque previous layer, so transparent PNGs don't double the brightness. */
(function () {
    const slider = document.getElementById('versionSlider');
    if (!slider) return;
    const stage = document.getElementById('renderStage');
    const output = document.getElementById('versionOutput');
    const views = [...document.querySelectorAll('.render-view')];
    const stops = [...document.querySelectorAll('[data-version-stop]')];
    const names = ['Original concept','First flying version','Final version'];
    const angles = {top:'Top view',isometric:'Isometric view',frame:'Frame only'};
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
    let angle = 'top', position = 0, animation = 0;
    function render(value) {
        position = Math.max(0,Math.min(200,value));
        const segment = Math.min(1,Math.floor(position/100));
        const blend = (position-segment*100)/100;
        views.forEach(view => {
            view.querySelectorAll('img').forEach((img,i) => {
                img.style.opacity = i===segment ? 1 : i===segment+1 ? blend : 0;
            });
        });
        const exact = Math.round(position/100);
        const label = Math.abs(position-exact*100)<.5 ? names[exact]
            : names[segment]+' → '+names[segment+1]+' · '+Math.round(blend*100)+'%';
        output.textContent = label;
        slider.setAttribute('aria-valuetext',label);
        stage.setAttribute('aria-label',angles[angle]+': '+label);
        stops.forEach(b => b.setAttribute('aria-pressed',String(Math.abs(position-Number(b.dataset.versionStop))<.5)));
    }
    slider.addEventListener('input', () => {
        cancelAnimationFrame(animation); render(Number(slider.value));
    });
    stops.forEach(button => button.addEventListener('click', () => {
        cancelAnimationFrame(animation);
        const start = position, target = Number(button.dataset.versionStop), started = performance.now();
        function tick(now) {
            const t = reducedMotion.matches ? 1 : Math.min(1,(now-started)/650);
            const eased = t*t*(3-2*t);
            const value = start+(target-start)*eased;
            slider.value = value; render(value);
            if (t<1) animation = requestAnimationFrame(tick);
        }
        animation = requestAnimationFrame(tick);
    }));
    document.querySelectorAll('[data-render-view]').forEach(button => {
        button.addEventListener('click', () => {
            angle = button.dataset.renderView;
            views.forEach(view => { view.hidden = view.dataset.view!==angle; });
            document.querySelectorAll('[data-render-view]').forEach(b => b.setAttribute('aria-pressed',String(b===button)));
            render(position);
        });
    });
    render(0);
})();
