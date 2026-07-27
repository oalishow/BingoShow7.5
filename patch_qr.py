import re

with open("index.tsx") as f:
    tsx = f.read()

replacement = """                    let basePath = window.location.pathname;
                    if (basePath.endsWith('index.html')) {
                        basePath = basePath.replace('index.html', '');
                    }
                    if (!basePath.endsWith('/')) {
                        basePath += '/';
                    }
                    const attendeeUrl = `${window.location.origin}${basePath}attendee.html?event=${encodeURIComponent(appStore.state.appConfig.eventId || "default")}`;
                    let qrDataUrl = "";
                    try {
                        qrDataUrl = await QRCode.toDataURL(attendeeUrl, { width: 140, margin: 1 });
                    } catch (e) {}"""

tsx = re.sub(
    r"const cardUrl = window\.location\.origin \+ window\.location\.pathname \+ \"\?card=\" \+ uuid;.*?catch \(e\) \{\}",
    replacement,
    tsx,
    flags=re.DOTALL
)

with open("index.tsx", "w") as f:
    f.write(tsx)
