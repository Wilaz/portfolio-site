<script lang="ts">
	import type { AvailableLanguageTag } from '$lib/paraglide/runtime';
	import { i18n } from '$lib/i18n';
	import { page } from '$app/stores';
	import { goto } from '$app/navigation';
	import { languageTag } from '$lib/paraglide/runtime.js';
	import { setLanguageTag } from '$lib/paraglide/runtime.js';
	import * as m from '$lib/paraglide/messages.js';

	function switchToLanguage(newLanguage: AvailableLanguageTag) {
		const canonicalPath = i18n.route($page.url.pathname);
		const localisedPath = i18n.resolveRoute(canonicalPath, newLanguage);
		goto(localisedPath);
	}
	const en: AvailableLanguageTag = 'en'
</script>

<div class="navbar bg-base-100">
	<div class="flex-1">
		<a class="btn btn-ghost text-xl" href="/">daisyUI</a>
	</div>
	<div class="flex-none">
		<ul class="menu menu-horizontal px-1">
			<li><a href="/about">about</a></li>
			<li><a href="/projects">projects</a></li>
			<li><a href="/contact">contact</a></li>
			{#if languageTag() == en}
				<button onclick={() => switchToLanguage('fr')}>fr</button>
			{:else}
				<button onclick={() => switchToLanguage('en')}>en</button>
			{/if}
		</ul>
	</div>
</div>
