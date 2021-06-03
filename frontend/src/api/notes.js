import to from 'await-to-js';

export default axios => ({
    async get() {
        const [error, response] = await to(axios.get(`/api/v1/notepad/notes/`));
        return [error, response?.data?.results];
    },

    async add(content) {
        const [error, response] = await to(axios.post(`/api/v1/notepad/notes/`, content));

        return [error, response];
    },
});
