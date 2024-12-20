<script lang="ts">
	import Check from '@componets/check.svelte';
	import Noncheck from '@componets/noncheck.svelte';
</script>

<h1 class="m-4 flex items-center justify-center text-5xl font-bold">My journey!</h1>

<ul class="timeline timeline-vertical timeline-snap-icon m-8 max-md:timeline-compact">
	<li>
		<div class="timeline-middle">
			<Check />
		</div>
		<div class="timeline-start mb-10 md:text-end">
			<time class="font-mono italic">2008</time>
			<div class="text-lg font-black">Birth</div>
			A child is born
		</div>
		<hr class="bg-primary" />
	</li>
	<li>
		<hr class="bg-primary" />
		<div class="timeline-middle">
			<Check />
		</div>
		<div class="timeline-end mb-10">
			<time class="font-mono italic">2012</time>
			<div class="text-lg font-black">Elementry school</div>
			I begain elementry school
		</div>
		<hr class="bg-primary" />
	</li>
	<li>
		<hr class="bg-primary" />
		<div class="timeline-middle">
			<Check />
		</div>
		<div class="timeline-start mb-10 md:text-end">
			<time class="font-mono italic">2016</time>
			<div class="text-lg font-black">Started scratch</div>
			I began programming using scratch
		</div>
		<hr class="bg-primary" />
	</li>
	<li>
		<hr class="bg-primary" />
		<div class="timeline-middle">
			<Check />
		</div>
		<div class="timeline-end mb-10">
			<time class="font-mono italic">2022</time>
			<div class="text-lg font-black">Highschool</div>
			I graduated elementry school and begin high school
		</div>
		<hr />
	</li>
	<li>
		<hr />
		<div class="timeline-middle">
			<Noncheck />
		</div>
		<div class="timeline-start mb-10 md:text-end">
			<time class="font-mono italic">2037</time>
			<div class="text-lg font-black">World domination</div>
			Control of the world is seized, java is banned.
		</div>
	</li>
</ul>
