# triage.py - Improved general keyword classifier

def triage(text):
    text = text.lower()

    # Preventive: internal restructuring without a requested
    # functional change.
    if (
        "no ticket or request" in text
        or "no behaviour change" in text
        or "no behavior change" in text
    ):
        return "preventive"

    # Corrective: repairing an existing fault or incorrect result.
    if any(word in text for word in [
        "wrong", "abends", "short", "failed", "incorrect", "error"
    ]):
        return "corrective"

    # Adaptive: responding to changes in the external environment.
    if any(word in text for word in [
        "bank changes", "file format", "mainframe upgrade",
        "regulator requires", "bank retires",
        "new secure service", "old sort utility"
    ]):
        return "adaptive"

    # Perfective: adding or improving requested functionality.
    if any(word in text for word in [
        "request", "requests"
    ]):
        return "perfective"

    return "unclassified"
