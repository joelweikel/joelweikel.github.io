"""Source material for the static MMORP Wiki. Run build.py after editing."""
from collections import OrderedDict

CATEGORIES = OrderedDict([
    ("characters", ("Characters", "The familiar faces, friends, and things trying to end your run.")),
    ("games", ("Games & mechanics", "From the original Scratch game to the jump into three dimensions.")),
    ("world", ("World & lore", "Places, stories, and the peculiar geography surrounding MMORP.")),
    ("joeltech", ("Joeltech", "The company, its headquarters, and its extremely ambitious products.")),
])

ARTICLES = []

def section(title, *paragraphs, bullets=None):
    return {"title": title, "paragraphs": list(paragraphs), "bullets": bullets or []}

def add(slug, title, category, summary, image, *,
        alt="", art=False, facts=(), sections=(), related=(), gallery=(), aliases=(), links=(), video=None):
    ARTICLES.append({
        "slug": slug, "title": title, "category": category, "summary": summary,
        "image": image, "alt": alt or title, "art": art, "facts": list(facts),
        "sections": list(sections), "related": list(related), "gallery": list(gallery),
        "aliases": list(aliases), "links": list(links), "video": video,
    })

add("mmorp", "MMORP", "characters",
    "The unmistakable face at the center of the series.",
    "mmorp.webp", art=True,
    alt="A three-dimensional render of MMORP",
    facts=[("Role", "Protagonist"), ("Appears in", "All MMORP games"), ("Also seen in", "Starschlop and other projects")],
    sections=[
        section("About", "MMORP is the main character of the MMORP series and the player’s character throughout its games. His shape has been compared to a heart, although his design has a character all its own.",
            "His appearance has changed with the series: the colorful Scratch original became a fully modeled character in [[mmorp-3d|MMORP 3D]]."),
        section("In the games", "In [[mmorp-1|the original game]], MMORP dodges ten levels of enemies using the keyboard. [[mmorp-3|MMORP 3]] moved the character toward the mouse, a control scheme continued in MMORP 3D."),
        section("Beyond the games", "MMORP appears in other projects, including Starschlop. In [[german-story|the German story]], he meets Orange Orange at the Derelict Camp and offers him a place with better Wi-Fi."),
    ],
    gallery=[("mmorp-classic.webp", "MMORP’s classic Scratch-era appearance."), ("mmorp3d.webp", "The MMORP 3D title screen.")],
    related=["mmorp-1", "mmorp-3d", "german-story"])
add("squelch", "Squelch", "characters",
    "The first enemy, and a very persistent one.",
    "squelch.webp", art=True,
    facts=[("First appears", "[[mmorp-1|MMORP]]"), ("Classic level", "1"), ("Also appears in", "[[mmorp-3d|MMORP 3D]]")],
    sections=[
        section("Behavior", "Squelches are the first enemies in the original MMORP and in MMORP 3D’s classic mode. They emerge from a ball and travel in straight paths.",
            "In MMORP 3D they can also hatch from Squelch eggs. Several enemy sources can produce them, making Squelches one of the most common threats in the game."),
        section("Strategy", "Keep an eye on where a Squelch starts moving: its straight path makes its direction useful information when finding a gap."),
    ], gallery=[("squelch-classic.svg", "Squelch as drawn for the original game.")],
    related=["mmorp-1", "mmorp-3d", "plopper"])
add("plopper", "Plopper", "characters",
    "An iconic second-level enemy that drops from above.",
    "plopper.webp", art=True,
    facts=[("First appears", "[[mmorp-1|MMORP]]"), ("Classic level", "2"), ("Related to", "[[toother|Toother]]")],
    sections=[
        section("Behavior", "The Plopper is the second enemy in the original MMORP. Its signature move is simple: it falls from the ceiling.",
            "Ploppers return in MMORP 3D. The faster [[toother|Toother]] is related to them and is described as their friend."),
    ], gallery=[("plopper-classic.svg", "A Plopper from the original MMORP.")],
    related=["squelch", "toother", "mmorp-1"])
add("threnemy", "Threnemy", "characters",
    "A wave of three, launched from a spinning wheel.",
    "threnemy.webp", art=True,
    facts=[("Also known as", "Tak"), ("Classic level", "3"), ("Damage", "1"), ("Appears in", "[[mmorp-1|MMORP]] and [[mmorp-3d|MMORP 3D]]")],
    sections=[
        section("Behavior", "The Threnemy, also called a Tak, is the third enemy in the original game and MMORP 3D’s classic mode. A spinning wheel sends Taks out in waves of three.",
            "In the original game, they travel toward the position MMORP occupied when they began moving, at varying speeds. In MMORP 3D, some have a limited ability to turn."),
        section("Variants and relatives", "A rare two-headed version appears in MMORP 3D. Threnemies are related to [[helper|Helpers]], though the two make very different first impressions."),
    ], gallery=[("threnemy-wheel.webp", "The Threnemy spawner in MMORP 3D."), ("threnemy-two-heads.webp", "A rare two-headed version."), ("threnemy-classic.svg", "A Threnemy from the original game."), ("threnemy-wheel-classic.svg", "The original spinning wheel.")],
    related=["helper", "tennemy", "mmorp-3d"], aliases=["tak"])
add("helper", "Helper", "characters",
    "A rare moment when running into an enemy is a good idea.",
    "helper.webp", art=True,
    facts=[("Classic level", "4"), ("Damage", "−0.5"), ("Appears in", "[[mmorp-1|MMORP]] and [[mmorp-3d|MMORP 3D]] classic mode")],
    sections=[
        section("Behavior", "Helpers spawn at random positions and orientations. Unlike most enemies, they deal negative damage: touching one restores health.",
            "Their level works as a mid-game breather, giving players a chance to stock up before the more dangerous [[chomper|Chompers]]. Helpers do not appear in MMORP 3D’s infinite mode."),
        section("Connections", "Helpers are related to [[threnemy|Threnemies]]. According to an in-universe rumor, [[prickly|Prickly]] projectiles grow up to become Helpers because of their similar appearance."),
    ], gallery=[("helper-classic.svg", "A Helper from the original game.")],
    related=["threnemy", "chomper", "prickly"])
add("chomper", "Chomper", "characters",
    "A patient pair with a very sudden bite.",
    "chomper.webp", art=True,
    facts=[("Classic level", "5"), ("Usually appears", "In pairs"), ("Appears in", "[[mmorp-1|MMORP]] and [[mmorp-3d|MMORP 3D]]")],
    sections=[
        section("Behavior", "Chompers spawn in pairs facing MMORP, pause, and then lunge forward to bite. They appear in both the original game and MMORP 3D.",
            "The level follows the restorative [[helper|Helper]] encounter, so its sudden increase in danger can catch players who have relaxed."),
    ], gallery=[("chomper-open.svg", "A Chomper with its mouth open."), ("chomper-closed.svg", "A Chomper with its mouth closed.")],
    related=["helper", "wall", "mmorp-1"])
add("wall", "Wall", "characters",
    "A five-damage obstacle and the end of many runs.",
    "wall.svg", art=True,
    facts=[("Classic level", "6"), ("Damage", "5"), ("Appears in", "[[mmorp-1|MMORP]]")],
    sections=[
        section("Behavior", "The Wall moves across the screen, creating an obstacle reminiscent of Flappy Bird. It deals five damage, enough to end many runs after the Chomper level.",
            "The Wall is the first enemy in the original sequence that is exclusive to the first game."),
    ], related=["chomper", "momo", "mmorp-1"])
add("momo", "Momo", "characters",
    "A side-profile enemy hiding beyond the Wall.",
    "momo.svg", art=True,
    facts=[("Classic level", "7"), ("Appears in", "[[mmorp-1|MMORP]]"), ("Attack", "A line of arrow-shaped projectiles")],
    sections=[
        section("Behavior", "Momo moves to a random point and fires a line of arrow-shaped projectiles at MMORP. Its side-profile appearance makes it visually unusual among the original enemies.",
            "Momo is less familiar to many players because reaching it means surviving the [[wall|Wall]] first."),
    ], gallery=[("momo-projectile.svg", "Momo’s projectile.")],
    related=["wall", "prickly", "mmorp-1"])
add("prickly", "Prickly", "characters",
    "A fast-moving pursuer with a steady supply of projectiles.",
    "prickly.svg", art=True,
    facts=[("Classic level", "8"), ("Appears in", "[[mmorp-1|MMORP]]"), ("Attack", "Aimed projectiles")],
    sections=[
        section("Behavior", "Prickly is a fast spawner that follows MMORP while firing projectiles toward him. Managing both the pursuer and its shots makes this a demanding late-game encounter."),
        section("The Helper rumor", "A bit of MMORP lore says that Prickly’s projectiles grow up to become [[helper|Helpers]]. The resemblance is there, but the connection is presented as a rumor."),
    ], gallery=[("prickly-projectile.svg", "A projectile spawned by Prickly.")],
    related=["helper", "derek", "mmorp-1"], aliases=["prickler"])
add("derek", "Derek", "characters",
    "A relaxed presence with a less relaxed projectile attack.",
    "derek.svg", art=True,
    facts=[("Classic level", "9"), ("Appears in", "[[mmorp-1|MMORP]]"), ("Attack", "Projectile bursts")],
    sections=[
        section("Behavior", "Derek sits in the middle of the screen and sends bursts of projectiles toward MMORP. He is dangerous, although the original notes describe some earlier levels as more difficult."),
    ], gallery=[("derek-projectile.svg", "One of Derek’s projectiles.")],
    related=["prickly", "tennemy", "mmorp-1"])
add("tennemy", "Tennemy", "characters",
    "The original game’s formidable tenth and final enemy.",
    "tennemy.svg", art=True,
    facts=[("Also known as", "Tak2"), ("Classic level", "10"), ("Appears in", "[[mmorp-1|MMORP]]")],
    sections=[
        section("Behavior", "Tennemy, also known as Tak2, is the most powerful enemy in the original MMORP. Tennemies appear across the map facing MMORP instead of emerging from the [[threnemy|Threnemy]] wheel.",
            "They resemble darker, more heavily eyed Threnemies but deal twenty times as much damage. They can often end a run in three hits or fewer."),
        section("Reputation", "The tenth level gained a reputation for being impossible to beat, and real-money rewards were offered to anyone who could clear it. Tennemies also appear on the original game’s splash art."),
    ], related=["threnemy", "evtest", "mmorp-1"], aliases=["tak2"])
add("gulper", "Gulper", "characters",
    "A slow-moving MMORP 3D enemy with two distinct variants.",
    "gulper.webp", art=True,
    facts=[("Appears in", "[[mmorp-3d|MMORP 3D]]"), ("Variants", "Tongued and toothed"), ("Spawn", "Spawner ball")],
    sections=[
        section("Behavior", "Gulpers move slowly toward the player and spawn from a spawner ball. They are exclusive to MMORP 3D."),
        section("Variants", "The tongued Gulper fires a smelly projectile. The toothed Gulper does not, so the two variants create different threats despite their similar movement."),
    ], related=["mmorp-3d", "toother"])
add("toother", "Toother", "characters",
    "A faster falling relative of the Plopper.",
    "toother.webp", art=True,
    facts=[("Appears in", "[[mmorp-3d|MMORP 3D]] infinite mode"), ("Movement", "Falls at twice the Plopper’s speed")],
    sections=[
        section("Behavior", "Toother is a falling enemy found in MMORP 3D’s infinite mode. It resembles the [[plopper|Plopper]], but falls twice as fast."),
        section("Relationships", "Toother is related to the [[spiker|Spiker]] but does not like it. Toother is friends with the Ploppers."),
    ], related=["plopper", "spiker", "mmorp-3d"])
add("spiker", "Spiker", "characters",
    "A fat, slow-moving creature that leaves Squelch eggs in its trail.",
    "spiker.webp", art=True,
    facts=[("Appears in", "[[mmorp-3d|MMORP 3D]]"), ("Movement", "Very slow, with difficulty turning")],
    sections=[
        section("Behavior", "Spikers are fat creatures that travel very slowly and have difficulty turning. They lay eggs in their trail that grow into [[squelch|Squelches]]."),
        section("Relationships", "Spikers are friends with [[orange-orange|Orange Orange]]."),
    ], gallery=[("spiker-top.webp", "Spiker viewed from above.")],
    related=["squelch", "orange-orange", "toother", "mmorp-3d"])
add("slim", "Slim", "characters",
    "The eccentric, dangerous inhabitant of the Derelict Camp.",
    "slim-photo.jpg",
    facts=[("Home", "[[derelict-camp|Derelict Camp]]"), ("Related to", "[[edina|Edina]]"), ("Reputation", "Dangerous and untrustworthy")],
    sections=[
        section("About", "Slim is the main inhabitant of the [[derelict-camp|Derelict Camp]] and is described as eccentric, dangerous, and inclined to consume everything in his path. He effectively runs the camp and sometimes wears shades."),
        section("In the stories", "In [[german-story|the German story]], Slim interrupts MMORP and Orange Orange’s visit to the camp. The two escape in MMORP’s MiG-25.",
            "The MMORP 3D notes also include an in-universe story in which a version of [[john-harper|John Harper Tarleton]] is trapped at the camp and consumed by Slim."),
    ], related=["edina", "derelict-camp", "german-story"])
add("edina", "Edina", "characters",
    "A beloved camp resident with a misleadingly evil name.",
    "edina.webp",
    facts=[("Home", "[[derelict-camp|Derelict Camp]]"), ("Related to", "[[slim|Slim]]"), ("Favorite activity", "Sleeping")],
    sections=[
        section("About", "Edina is related to Slim and lives at the Derelict Camp. The E in her name is said to stand for “evil,” but her actual interests are much gentler: staying indoors and sleeping, especially on couches."),
    ], gallery=[("edina-clothes.webp", "Edina resting among clothes."), ("edina-house.webp", "Edina’s house at the camp.")],
    related=["slim", "derelict-camp"])
add("john-harper", "John Harper Tarleton", "characters",
    "Musician, MMORP 3D collaborator, and a figure in the lore.",
    "john-harper.webp",
    facts=[("Also known as", "Anonymous Fruit Bat"), ("Contribution", "Music for [[mmorp-3d|MMORP 3D]]")],
    sections=[
        section("Music", "John Harper Tarleton, also known as Anonymous Fruit Bat, is a musical artist who helped compose the music for MMORP 3D."),
        section("In the MMORP universe", "The game’s notes also feature an in-universe version of John Harper in a story involving [[slim|Slim]] and the [[derelict-camp|Derelict Camp]]. The fictional account is separate from his real-world music credit."),
    ], related=["mmorp-3d", "slim", "derelict-camp"], aliases=["anonymous fruit bat"])
add("orange-orange", "Orange Orange", "characters",
    "Tyler, a would-be meme with an urgent need for better Wi-Fi.",
    "orange-orange.webp",
    facts=[("Real name", "Tyler"), ("Story appearance", "[[german-story|The German Story]]")],
    sections=[
        section("About", "Orange Orange, whose real name is Tyler, wanted to become a meme, although it never caught on."),
        section("The German story", "In [[german-story|the German story]], Orange Orange wanders into the Derelict Camp while playing Clash Royale. MMORP offers him better Wi-Fi; after Slim appears, the two leave in a MiG-25."),
    ], related=["german-story", "mmorp", "slim"], aliases=["tyler", "orange squared"])

add("mmorp-1", "MMORP", "games",
    "The Scratch original: ten levels, countless projectiles, one infamous finale.",
    "mmorp1-splash.webp",
    facts=[("Released", "December 2021"), ("Engine", "Scratch"), ("Levels", "10"), ("Controls", "WASD or arrow keys")],
    sections=[
        section("Overview", "The original MMORP began the series as a Scratch game about dodging projectiles through ten enemy levels. It became popular to play in class and inspired copycats and spin-offs.",
            "The final [[tennemy|Tennemy]] level became notorious for its difficulty. The creator’s notes describe a win screen that was effectively unreachable, even with developer tools."),
        section("How to play", "Move MMORP with WASD or the arrow keys and dodge the enemies. Press B to turn randomly. The character can wrap around the edges of the screen.",
            "The game may contain flashing lights."),
        section("Evtest and development", "[[evtest|Evtest]] opens a passcode prompt for developer modes and cheats. The original Scratch notes list billy for 100 lives and EZ for easy mode; yes enables a health-regenerating developer mode.",
            "The project’s code uses several different approaches to enemy behavior. Its experimental construction is part of the original’s history."),
        section("Enemy order", "The original ten levels are [[squelch|Squelch]], [[plopper|Plopper]], [[threnemy|Threnemy]], [[helper|Helper]], [[chomper|Chomper]], [[wall|Wall]], [[momo|Momo]], [[prickly|Prickly]], [[derek|Derek]], and [[tennemy|Tennemy]]."),
    ], gallery=[("mmorp1-gameplay.webp", "A scene from the original game."), ("mmorp1-death.webp", "The original death screen."), ("mmorp1-win.webp", "The elusive win screen.")],
    related=["mmorp", "evtest", "mmorp-3", "mmorp-3d"],
    aliases=["mmorp 1", "original mmorp"],
    links=[("Play on Scratch", "https://scratch.mit.edu/projects/612511851/")])
add("mmorp-2", "MMORP 2", "games",
    "The unusual middle entry in the original trilogy.",
    "mmorp2.webp",
    facts=[("Format", "Visual Basic script"), ("Series", "Original MMORP trilogy"), ("Archive status", "Limited documentation")],
    sections=[
        section("Overview", "MMORP 2 is considered part of the original trilogy. The source notes describe it as malware distributed as a Visual Basic script, rather than a conventional game.",
            "The archive contains very little additional information about this entry. No script is included with this wiki."),
    ], related=["mmorp-1", "mmorp-3"])
add("mmorp-3", "MMORP 3", "games",
    "The unfinished Scratch sequel that introduced mouse movement.",
    "mmorp3.webp",
    facts=[("Published", "May 2022 gameplay test"), ("Engine", "Scratch"), ("Status", "Unfinished"), ("Controls", "Mouse")],
    sections=[
        section("Overview", "MMORP 3 was the final entry in the original Scratch trilogy and remained unfinished. It introduced a more advanced menu, new levels, skins, and a revised movement system."),
        section("Movement and settings", "Rather than moving directly with the arrow keys, MMORP follows the mouse with a smoothing effect. This change also removed the original game’s screen wrapping.",
            "Video settings include pixelation, a fisheye-like warp, and color changes. Some of those effects originated as experimental settings in the first game’s [[evtest|Evtest]] mode."),
        section("Versions", "The project included a gameplay test and a “deduxe” version associated with Wii U and Joel’s website. The Wii U version was not publicly released, according to the project notes."),
    ], gallery=[("mmorp3-deluxe.webp", "MMORP 3 “deduxe” artwork."), ("mmorp3-wiiu.webp", "MMORP 3 shown on a Wii U screen.")],
    related=["mmorp-1", "evtest", "mmorp-3d"],
    links=[("Play the gameplay test", "../MMORP%203%20(gameplay%20Test)(1).html")])
add("mmorp-3d", "MMORP 3D", "games",
    "The original’s bullet-hell chaos, rebuilt in Unreal Engine 5.",
    "mmorp3d.webp",
    facts=[("Released", "October 23, 2024"), ("Engine", "Unreal Engine 5"), ("Platform", "Windows"), ("Controls", "Mouse"), ("Combinations", "781 possible enemy combinations")],
    sections=[
        section("Overview", "MMORP 3D began as a remake of [[mmorp-1|the original MMORP]] with path tracing and Blender-made assets. It grew into a three-dimensional game with randomized encounters, new enemies, and new mechanics.",
            "The game includes classic and infinite modes. The creator’s notes list 781 possible enemy combinations, with music contributed by [[john-harper|John Harper Tarleton]]."),
        section("How to play", "Move the mouse to guide MMORP, dodge enemies, and survive. Classic mode revisits enemies from the original, while infinite mode introduces threats such as [[toother|Toother]]."),
        section("Creatures", "Returning enemies include [[squelch|Squelch]], [[plopper|Plopper]], [[threnemy|Threnemy]], [[helper|Helper]], and [[chomper|Chomper]]. Newer creatures include [[gulper|Gulper]] and Toother."),
    ], gallery=[("mmorp3d-green.webp", "A green MMORP 3D arena."), ("mmorp3d-red.webp", "A red MMORP 3D arena."), ("mmorp3d-blue.webp", "Enemies in a blue arena.")],
    related=["mmorp", "mmorp-1", "john-harper", "gulper"],
    links=[("View on itch.io", "https://perkanover.itch.io/mmorp-3d")])
add("kafkaesque", "Kafkaesque Game", "games",
    "A sprawling experiment in terrain, vehicles, building, and fracking.",
    "kafkaesque.webp",
    facts=[("Published", "April 14, 2024"), ("Engine", "Unreal Engine 5"), ("Platform", "Windows"), ("Status", "Prototype")],
    sections=[
        section("Overview", "Kafkaesque Game was Joel’s first Unreal Engine 5 game: a collection of systems built while learning. It combines randomly generated terrain and structures with building, ground vehicles, and aircraft."),
        section("Getting started", "Punch trees for Smart Coins, build a fracker for passive oil income, and put up turrets for protection. From there, build more frackers, a vehicle creator, or whatever the situation calls for."),
        section("Controls", "Use WASD to move, left click for a melee attack, Space to fire, Tab to switch view, E to interact, and Q to enter build mode. The scroll wheel cycles through build options."),
        section("Vehicles and structures", "The vehicle roster includes the F-22, MiG-31, MiG-29, Su-47, F-104, La-11, Wright Flyer, a Tartarian aircraft, and a dune buggy. The world also contains turrets, castles, frackers, and a memorial Kafka Stone."),
    ], gallery=[("kafkaesque-cockpit.webp", "An aircraft cockpit."), ("kafkaesque-fracker.webp", "Frackers in the landscape."), ("kafkaesque-mig.webp", "A MiG turning in flight."), ("kafkaesque-terrain.webp", "Procedurally generated terrain.")],
    related=["mmorp-3d"], links=[("View on itch.io", "https://perkanover.itch.io/kafkaesque-game")])
add("evtest", "Evtest", "games",
    "The original game’s passcode-powered developer menu.",
    "mmorp1-gameplay.webp",
    facts=[("First appears", "[[mmorp-1|MMORP]]"), ("Type", "Developer mode and cheats")],
    sections=[
        section("Overview", "Evtest is a recurring developer feature that asks for a passcode and enables different tools or cheats. Its name is a play on “devtest.”"),
        section("Known codes", "In the original game, yes answers the button’s “Evtest?” prompt and enables a mode that adds one health per tick. Even that regeneration may not save the player from [[tennemy|Tennemy]].",
            "The original Scratch notes also list billy for 100 lives and EZ for easy mode. These can help players practice enemy patterns."),
        section("Visual effects", "Some experimental visual settings from the first game later appeared in [[mmorp-3|MMORP 3]], including pixelation, warp, and color changes."),
    ], related=["mmorp-1", "mmorp-3", "tennemy"], aliases=["devtest", "cheats", "yes", "billy", "EZ"])

add("derelict-camp", "Derelict Camp", "world",
    "A not entirely welcoming camp at the heart of the lore.",
    "derelict-camp.webp",
    facts=[("Main inhabitant", "[[slim|Slim]]"), ("Other resident", "[[edina|Edina]]"), ("Appears in", "[[german-story|The German Story]]")],
    sections=[
        section("Overview", "The Derelict Camp is a recurring location associated with Slim and Edina. Slim is its main inhabitant, while Edina’s house is also found at the camp."),
        section("Stories and surroundings", "In [[german-story|the German story]], Orange Orange arrives at the camp, meets MMORP, and eventually flees with him when Slim appears.",
            "Signs at the camp point toward [[mobile-alabama|Mobile, Alabama]], although the lore warns that following them will not get an ordinary traveler there. The [[darna|Darna clan]] is described as a force seeking to take over and end the camp."),
    ], gallery=[("derelict-camp-sign.webp", "A Derelict Camp sign."), ("edina-house.webp", "Edina’s house.")],
    video=("derelict-camp-ost.mp4", "derelict-camp-sign.webp", "The Derelict Camp outskirts, with music from the archive."),
    related=["slim", "edina", "mobile-alabama", "darna"])
add("darna", "Darna", "world",
    "The base of a clan with designs on the Derelict Camp.",
    "darna.webp", art=True,
    facts=[("Associated group", "Darna clan"), ("Rival location", "[[derelict-camp|Derelict Camp]]")],
    sections=[
        section("The clan", "Darna is the base of the Darna clan, described in the MMORP lore as a powerful force trying to take over and end the [[derelict-camp|Derelict Camp]]."),
        section("Tactics", "The clan’s notes mention wall breakers and a “barb cycle” using evolved barbarians, including the top-secret evolved barb hut. The archive also preserves a Great Darna II clan description; its roster and statistics are a snapshot rather than necessarily current."),
    ], gallery=[("darna-hq.webp", "An image associated with Darna’s headquarters.")],
    related=["derelict-camp", "slim"])
add("archipelago", "Joeltech Archipelago", "world",
    "A volcanic island headquarters in the South Pacific.",
    "archipelago.webp",
    facts=[("Region", "South Pacific"), ("Landform", "Volcanic caldera"), ("Home to", "[[joeltech|Joeltech]] headquarters")],
    sections=[
        section("Geography", "The Joeltech Archipelago is a fictional island group near Henderson Island and Rapa in the South Pacific. The islands sit within a giant volcanic caldera and are home to chambered nautiluses and other mollusks."),
        section("Joeltech headquarters", "The archipelago is the location of [[joeltech|Joeltech]] headquarters and Joel’s home after founding the company. In the lore, it is independent of any country and protected by paramilitary groups under Joeltech’s control."),
    ], gallery=[("archipelago-fisheye.webp", "A wide view across the archipelago."), ("archipelago-night.webp", "The islands at night."), ("archipelago-map.webp", "An overhead view of the islands."), ("joeltech-hq.webp", "Joeltech headquarters.")],
    related=["joeltech", "gale", "joeltech-phone"], aliases=["joeltech archipeligo"])
add("mobile-alabama", "Mobile, Alabama", "world",
    "A celebrated destination, especially for one particular Moe’s.",
    "mobile.webp",
    facts=[("Known for", "Moe’s"), ("Connected to", "[[derelict-camp|Derelict Camp]]")],
    sections=[
        section("In the lore", "In MMORP lore, Mobile is celebrated as a place even better than heaven, with particular praise reserved for its Moe’s. Both Slim and John Harper are said to enjoy eating there."),
        section("Getting there", "Signs near the [[derelict-camp|Derelict Camp]] point toward Mobile, but the notes warn that following the signs will not work for everyone. They are intended for Slim."),
    ], gallery=[("mobile-sign.webp", "A sign pointing toward Mobile.")],
    related=["derelict-camp", "slim", "john-harper"], aliases=["moes"])
add("german-story", "The German Story", "world",
    "MMORP, Orange Orange, a dangerous camp, and the search for Wi-Fi.",
    "world-map.webp",
    facts=[("Written", "April 28, 2026"), ("Language", "German"), ("Setting", "[[derelict-camp|Derelict Camp]]")],
    sections=[
        section("Plot", "[[orange-orange|Orange Orange]] wanders into the Derelict Camp while playing Clash Royale. He meets [[mmorp|MMORP]], who offers him access to a better Wi-Fi connection at his house."),
        section("Escape", "A boom and a fire announce [[slim|Slim]]’s arrival. MMORP and Orange Orange escape in MMORP’s MiG-25 and fly away in search of good Wi-Fi."),
        section("Original", "The story was written in German. The original document is available below, and the summary here follows its events rather than translating every line."),
    ], related=["orange-orange", "mmorp", "slim", "derelict-camp"],
    links=[("Read the original story (PDF)", "assets/german-story.pdf")])

add("joeltech", "Joeltech", "joeltech",
    "A fictional company with big ideas and an island headquarters.",
    "joeltech-logo.webp",
    facts=[("Headquarters", "[[archipelago|Joeltech Archipelago]]"), ("Products", "[[gale|Gale]], [[joeltech-phone|Joeltech Phone]], [[mmorp-1|MMORP]]")],
    sections=[
        section("Overview", "Joeltech is a company in the MMORP universe. Its projects range from the MMORP games to a phone and the Gale supercar, with headquarters on the [[archipelago|Joeltech Archipelago]]."),
        section("Products", "The [[gale|Gale]] is a high-performance supercar with a Sprat trim. The [[joeltech-phone|Joeltech Phone]] pairs an extraordinary price with a JTX 6090 mobile chip. MMORP is also described in the archive as a Joeltech success."),
    ], gallery=[("joeltech-old-logo.webp", "An alternate Joeltech logo."), ("archipelago.webp", "The Joeltech Archipelago.")],
    related=["archipelago", "gale", "joeltech-phone", "mmorp-1"])
add("gale", "Joeltech Gale", "joeltech",
    "A twincharged V8 supercar with an even more ambitious Sprat trim.",
    "gale.webp",
    facts=[("Manufacturer", "[[joeltech|Joeltech]]"), ("Engine", "Twincharged V8"), ("Base output", "1,000 hp"), ("Base 0–60 mph", "3.0 seconds")],
    sections=[
        section("Overview", "The Gale is a Joeltech supercar powered by a twincharged Joeltech V8. The base model is rated in the project notes at 1,000 horsepower and a 0–60 mph time of 3.0 seconds."),
        section("Gale Sprat", "The Gale Sprat raises the stated output to 1,670 horsepower and the 0–60 mph time to 2.1 seconds. It also has a 170-horsepower electric motor driving the front wheels."),
    ], gallery=[("gale-sprat.webp", "The Gale Sprat."), ("gale-powertrain.webp", "The Gale’s powertrain and chassis."), ("gale-rear.webp", "A rear view of the Gale Sprat."), ("gale-engine.webp", "The Joeltech engine bay.")],
    related=["joeltech", "archipelago", "joeltech-phone"])
add("joeltech-phone", "Joeltech Phone", "joeltech",
    "An outrageously expensive phone with an equally outrageous chip.",
    "joeltech-phone.webp",
    facts=[("Manufacturer", "[[joeltech|Joeltech]]"), ("Listed price", "$9,999.99"), ("Chip", "JTX 6090 mobile")],
    sections=[
        section("Overview", "The Joeltech Phone is a Joeltech product listed at $9,999.99. The notes say its high price was unpopular with many users."),
        section("Hardware", "It includes a JTX 6090 mobile chip, described in the project’s tongue-in-cheek lore as making it the fastest phone ever made."),
    ], gallery=[("joeltech-phone-colors.webp", "Joeltech Phone promotional artwork.")],
    related=["joeltech", "gale"])
