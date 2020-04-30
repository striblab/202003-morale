<script>
  export let window_width;
  export let booster;
  export let store;

  let w = 300;
  let h = 400;

  function shorten(string) {
    var trimmedString = string.substr(0, 250);

    trimmedString = trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" ")))

    trimmedString = trimmedString + " (...)"

    return trimmedString
  }

  function open(booster) {
    var box = document.querySelector('.lightbox');
    box.style.display = 'block'

    store.set(booster)
  }

</script>

  {#if booster.from_strib === "TRUE"}

    {#if booster.shape === "Portrait"}

      {#if booster.long === "TRUE"}

        <div class="card strib {booster.type} portrait long">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            {#if window_width > 900}
              <p>{@html shorten(booster.story)} <a href="{booster.url}" target="_blank">Read more</a></p>
            {:else}
              <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
            {/if}
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>
        </div>

      {:else}

        <div class="card strib {booster.type} portrait">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>
        </div>

      {/if}

    {:else}

      {#if booster.long === "TRUE"}
        <div class="card strib {booster.type} landscape long">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
            {#if window_width > 900}
              <p>{@html shorten(booster.story)} <a href="{booster.url}" target="_blank">Read more</a></p>
            {:else}
              <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
            {/if}
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>

        </div>
      {:else}
      <div class="card strib {booster.type} landscape">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
             <p>{@html booster.story} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
          </div>

        </div>
      {/if}

    {/if}

  {:else}

    {#if booster.shape === "Portrait"}

      {#if booster.long === "TRUE"}

        <div class="card {booster.type} portrait long">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            {#if window_width > 900}
            <p>{@html shorten(booster.story)}</p>
            <div class="readMore" on:click={open(booster)}>
        			<p>Read more</p>
        		</div>
            {:else}
            <p>{@html booster.story}</p>
            {/if}
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>
        </div>

      {:else}

        <div class="card {booster.type} portrait">
          <h5 class="stamp">{booster.timestamp}</h5>
          <video height="400" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
            <source src="{booster.asset}" type="video/quicktime">
          </video>
          <div class="text">
            <p>{@html booster.story}</p>
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>
        </div>

      {/if}

    {:else}

      {#if booster.long === "TRUE"}
        <div class="card {booster.type} landscape long">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
            {#if window_width > 900}
            <p>{@html shorten(booster.story)}</p>
            <div class="readMore" on:click={open(booster)}>
             <p>Read more</p>
           </div>
            {:else}
            <p>{@html booster.story}</p>
            {/if}
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>

        </div>
      {:else}
      <div class="card strib {booster.type} landscape">
          <h5 class="stamp">{booster.timestamp}</h5>

          <video height="300" src="{booster.asset}" controls>
            <source src="{booster.asset}" type="video/mp4">
          </video>
          <div class="text">
             <p>{@html booster.story}</p>
          <h4 class="author">{booster.name}, {booster.city}</h4>
          </div>

        </div>
      {/if}

    {/if}

  {/if}
