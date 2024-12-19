import adapter from '@sveltejs/adapter-auto';
import path from 'path';
import { mdsvex } from 'mdsvex';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
export default {
	preprocess: [vitePreprocess(), mdsvex()],

	compilerOptions: {
		runes: true
	},

	kit: {
		adapter: adapter(),
		alias: {
			'@componets': path.resolve('./src/componets')
		}
	},

	extensions: ['.svelte', '.svx']
};
