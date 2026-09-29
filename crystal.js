/* Crystal study. No 3D library: rotate points, project them, draw text.
   FCC = corners + face centers. HCP = alternating hexagonal A/B layers.
   Repeated positions are deduplicated where neighboring cells share atoms. */
(function () {
    const canvas = document.getElementById('crystalCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;
    const section = document.getElementById('crystalSection');
    const description = document.getElementById('crystalDescription');
    const readout = document.getElementById('latticeReadout');
    const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)');
    let angleX = -.4, angleY = .55, paused = reducedMotion.matches;
    let atoms = [], bonds = [], kind = 'fcc', width = 500, height = 500;
    let dragging = false, lastX = 0, lastY = 0, visible = true, frame = 0, lastTime = 0;
    let spread = 0;

    function buildLattice(type) {
        atoms = [];
        if (type === 'hcp') {
            // Zinc's c/a ratio is about 1.856, rather than the ideal HCP ratio.
            // Each successive layer is half a unit cell higher; B sits in A's gaps.
            const layerHeight = 1.856 / 2;
            for (let layer = 0; layer < 5; layer++) {
                const offset = layer % 2;
                for (let q = -2; q <= 2; q++) for (let r = -2; r <= 2; r++) {
                    if (Math.abs(q+r) > 2) continue;
                    atoms.push([q+r/2 + offset*.5, (layer-2)*layerHeight,
                        r*Math.sqrt(3)/2 + offset*Math.sqrt(3)/6]);
                }
            }
            // Center the whole cluster without altering the layer geometry.
            const center = [0,1,2].map(k => atoms.reduce((sum,a) => sum+a[k],0)/atoms.length);
            atoms = atoms.map(a => a.map((v,k) => (v-center[k])*.8));
        } else {
            const basis = [[0,0,0],[0,.5,.5],[.5,0,.5],[.5,.5,0]];
            for (let x=0; x<=2; x++) for (let y=0; y<=2; y++) for (let z=0; z<=2; z++) {
                basis.forEach(b => {
                    const point = [x+b[0],y+b[1],z+b[2]];
                    if (point.every(v => v<=2)) atoms.push(point.map(v => (v-1)*1.3));
                });
            }
        }
        bonds = [];
        atoms.forEach((a,i) => {
            for (let j=i+1; j<atoms.length; j++) {
                const d = a.reduce((sum,v,k) => sum+(v-atoms[j][k])**2,0);
                // Include both basal and adjacent-layer neighbors for non-ideal zinc.
                if (type === 'hcp' ? d < .81 : Math.abs(d-.845)<.001) bonds.push([i,j]);
            }
        });
        kind = type;
        description.textContent = type === 'fcc'
            ? 'Copper has a face-centered cubic structure.'
            : 'Zinc has a hexagonal close-packed structure.';
        readout.textContent = type === 'fcc' ? 'Cu / FCC' : 'Zn / HCP';
        document.querySelectorAll('[data-lattice]').forEach(b => b.setAttribute('aria-pressed',String(b.dataset.lattice===type)));
        canvas.setAttribute('aria-label','Rotatable '+(type==='fcc' ? 'copper FCC' : 'zinc HCP')+' lattice. Drag or use arrow keys to rotate.');
        draw();
    }
    function project(point, index) {
        // Separation on scroll is a visual effect, not a physical model of melting.
        const f = 1 + spread * .6;
        let [x,y,z] = point.map(v => v*f);
        x += Math.sin(index*5.3) * spread * .35;
        y += Math.cos(index*3.1) * spread * .35;
        const rx = x*Math.cos(angleY) - z*Math.sin(angleY);
        const rz = x*Math.sin(angleY) + z*Math.cos(angleY);
        const ry = y*Math.cos(angleX) - rz*Math.sin(angleX);
        const depth = y*Math.sin(angleX) + rz*Math.cos(angleX);
        const scale = Math.min(width,height) * .165 * 7/(7+depth);
        return { x: width/2 + rx*scale, y: height/2 + ry*scale, z: depth, scale };
    }
    function draw() {
        ctx.clearRect(0,0,width,height);
        const points = atoms.map(project);
        // Subtle guide marks around the field.
        ctx.fillStyle = '#344b5766'; ctx.font = '10px monospace';
        [[20,25],[width-25,25],[20,height-20],[width-25,height-20]].forEach(p => ctx.fillText('+',...p));
        // The bonds are dotted ASCII lines, fading away as the block separates.
        ctx.font = '10px monospace'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
        ctx.fillStyle = 'rgba(68,77,80,' + (.25*(1-spread*.8)) + ')';
        bonds.forEach(([i,j]) => {
            const a = points[i], b = points[j];
            const steps = Math.floor(Math.hypot(a.x-b.x,a.y-b.y)/10);
            for (let k=1;k<steps;k++) ctx.fillText('.', a.x+(b.x-a.x)*k/steps, a.y+(b.y-a.y)*k/steps);
        });
        // Draw far atoms first, so the nearest symbols read more clearly.
        points.sort((a,b) => b.z-a.z).forEach(p => {
            const depth = Math.max(0,Math.min(1,(p.z+4)/8));
            ctx.fillStyle = kind === 'hcp'
                ? `rgba(18,88,155,${1-depth*.4})`
                : `rgba(158,72,33,${1-depth*.4})`;
            ctx.font = `600 ${Math.round(16-depth*4)}px monospace`;
            ctx.fillText(kind === 'hcp' ? 'Zn' : 'Cu',p.x,p.y);
        });
    }
    function resize() {
        const rect = canvas.getBoundingClientRect();
        width = rect.width; height = rect.height;
        const dpr = Math.min(devicePixelRatio || 1,2);
        canvas.width = Math.round(width*dpr); canvas.height = Math.round(height*dpr);
        ctx.setTransform(dpr,0,0,dpr,0,0); draw();
    }
    function tick(time) {
        frame = 0;
        if (!visible || document.hidden || paused || dragging) return;
        const dt = lastTime ? Math.min(time-lastTime,50) : 16;
        lastTime = time;
        angleY += dt*.00012;
        draw(); frame = requestAnimationFrame(tick);
    }
    function animate() {
        lastTime = 0;
        if (!frame && visible && !document.hidden && !paused && !dragging) frame = requestAnimationFrame(tick);
    }
    document.querySelectorAll('[data-lattice]').forEach(button => {
        button.addEventListener('click', () => buildLattice(button.dataset.lattice));
    });
    canvas.addEventListener('pointerdown', e => {
        dragging = true; lastX = e.clientX; lastY = e.clientY;
        canvas.setPointerCapture(e.pointerId);
    });
    canvas.addEventListener('pointermove', e => {
        if (!dragging) return;
        angleY += (e.clientX-lastX)*.008;
        angleX += (e.clientY-lastY)*.008;
        lastX=e.clientX; lastY=e.clientY; draw();
    });
    ['pointerup','pointercancel','lostpointercapture'].forEach(name => canvas.addEventListener(name, () => { dragging=false; animate(); }));
    canvas.addEventListener('keydown', e => {
        if (!['ArrowLeft','ArrowRight','ArrowUp','ArrowDown'].includes(e.key)) return;
        e.preventDefault();
        angleY += e.key === 'ArrowLeft' ? -.12 : e.key === 'ArrowRight' ? .12 : 0;
        angleX += e.key === 'ArrowUp' ? -.12 : e.key === 'ArrowDown' ? .12 : 0;
        draw();
    });
    function updateSpread() {
        const rect = section.getBoundingClientRect();
        const mobile = innerWidth <= 700;
        spread = reducedMotion.matches ? 0 : Math.max(0, Math.min(1, (82-rect.top)/(mobile ? rect.height*.8 : rect.height-innerHeight+82)));
        draw();
    }
    let scrollFrame = 0;
    addEventListener('scroll', () => {
        if (!scrollFrame) scrollFrame = requestAnimationFrame(() => { scrollFrame=0; updateSpread(); });
    }, {passive:true});
    reducedMotion.addEventListener('change', () => { paused=reducedMotion.matches; animate(); updateSpread(); });
    new ResizeObserver(resize).observe(canvas);
    new IntersectionObserver(entries => { visible=entries[0].isIntersecting; animate(); }).observe(canvas);
    document.addEventListener('visibilitychange', animate);
    buildLattice(Math.random() < .5 ? 'hcp' : 'fcc'); resize(); animate(); updateSpread();
})();
