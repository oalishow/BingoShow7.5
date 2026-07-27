import re

with open("index.tsx") as f:
    tsx = f.read()

# For classic floating number:
cleanup1 = """            const cleanup = () => {
                appStore.state.pendingNumber = null;
                appStore.debouncedFirebaseSync(true);
                document.removeEventListener('keydown', handleKeydown);
                clearTimeout(floatingNumberTimeout as ReturnType<typeof setTimeout>);
            };"""
tsx = tsx.replace("""            const cleanup = () => {
                document.removeEventListener('keydown', handleKeydown);
                clearTimeout(floatingNumberTimeout as ReturnType<typeof setTimeout>);
            };""", cleanup1)

# For sponsor modal:
cleanup2 = """            const cleanup = () => {
                appStore.state.pendingNumber = null;
                appStore.debouncedFirebaseSync(true);
                document.removeEventListener('keydown', handleKeydown);
                clearTimeout(sponsorTimeout as ReturnType<typeof setTimeout>);
            };"""
tsx = tsx.replace("""            const cleanup = () => {
                document.removeEventListener('keydown', handleKeydown);
                clearTimeout(sponsorTimeout as ReturnType<typeof setTimeout>);
            };""", cleanup2)

with open("index.tsx", "w") as f:
    f.write(tsx)
