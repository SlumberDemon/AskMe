export const actions = {
    default: async ({ request }) => {
        const formData = await request.formData()

        const key = formData.get('key')
        const reply = formData.get('reply')

        fetch(`/api/questions?key=${key}`, {
            method: 'PATCH',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({ reply: reply, replied: true })
        }).then(() => {
            // window.location.reload();
        });
    }
}