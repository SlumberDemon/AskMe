async function getQs() {
    const data = await fetch('/api/questions');
    let items = await data.json();
    return items;
}

export const items = getQs()