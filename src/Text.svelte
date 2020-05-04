<script>
export let window_width;
export let booster;
export let store;

function shorten(string) {
	var trimmedString = string.substr(0, 350);

	trimmedString = trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" ")))

	trimmedString = trimmedString

	return trimmedString
}

function open(booster) {
	var box = document.querySelector('.lightbox');
	box.style.display = 'block'

	store.set()
	store.set(booster)
}

</script>

{#if booster.from_strib === "TRUE"}

	{#if booster.long === "TRUE"}

	<div class="card strib {booster.type} long">
		<div class="text">
			<h5 class="stamp">{booster.timestamp} • <span class="green"><a href="{booster.url}" target="_blank">View story</a></span></h5>
			{#if window_width > 900}
				<p class="story">{@html shorten(booster.story)} <span class="readMore" on:click={open(booster)}>... Read more</span></p>
				<p></p>
			{:else}
				<p>{@html booster.story}Read more</p>
			{/if}
	        <h4 class="author">{booster.name}, Star Tribune</h4>
		</div>
	</div>

	{:else}

	<div class="card strib {booster.type}">
		<div class="text">
			<h5 class="stamp">{booster.timestamp} • <span class="green"><a href="{booster.url}" target="_blank">View story</a></span></h5>
			<p>{@html booster.story}</p>
	        <h4 class="author">{booster.name}, Star Tribune</h4>
		</div>
	</div>

	{/if}

{:else}

{#if booster.long === "TRUE"}

<div class="card {booster.type} long">
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
		{#if window_width > 900}
			<p class="story">{@html shorten(booster.story)} <span class="readMore" on:click={open(booster)}>... Read more</span></p>
		{:else}
			<p>{@html booster.story}</p>
		{/if}
      <h4 class="author">{booster.name}, {booster.city}</h4>
	</div>
</div>

{:else}

<div class="card {booster.type}">
	<div class="text">
		<h5 class="stamp">{booster.timestamp}</h5>
			<p>{@html booster.story}</p>
      <h4 class="author">{booster.name}, {booster.city}</h4>
	</div>
</div>

{/if}

{/if}
