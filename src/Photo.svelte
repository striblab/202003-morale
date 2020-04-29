<script>
  export let booster;
  export let store;

  let lightbox_booster

  let pWidth = 600;
  let pHeight = 1000;

  let lWidth = 1000;
  let lHeight = 600;

  let pUrl = booster.asset + '?w=' + pWidth + '&h=' + pHeight + '&fit=crop&crop=faces&max-h=900';
  let lUrl = booster.asset + '?w=' + lWidth + '&h=' + lHeight + '&fit=crop&crop=faces&max-h=600';

  function open(booster) {
    var box = document.querySelector('.lightbox');
    box.style.display = 'block'

    store.subscribe(value => {
  		lightbox_booster = booster;
  	});
    store.set(booster)
  }

  function shorten(string) {
    var trimmedString = string.substr(0, 250);

    trimmedString = trimmedString.substr(0, Math.min(trimmedString.length, trimmedString.lastIndexOf(" ")))

    trimmedString = trimmedString + " (...)"

    return trimmedString
  }
</script>

<style>

</style>

{#if booster.from_strib === "TRUE"}

  {#if booster.shape === "Portrait"}

    {#if booster.long === "TRUE"}
      <div class="card strib {booster.type} portrait long">
        <h5 class="stamp">{booster.timestamp}</h5>
        <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
        <div class="text">
          <p>{@html shorten(booster.story)} <a href="{booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{booster.name}, Star Tribune</h4>
        </div>
      </div>
    {:else}
      <div class="card strib {booster.type} portrait">
        <h5 class="stamp">{booster.timestamp}</h5>
        <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
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
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html shorten(booster.story)} <a href="{booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{booster.name}, Star Tribune</h4>
      </div>
    </div>
    {:else}
    <div class="card strib {booster.type} landscape">
      <h5 class="stamp">{booster.timestamp}</h5>
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
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
    <div class="card strib {booster.type} portrait long">
      <h5 class="stamp">{booster.timestamp}</h5>
      <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html shorten(booster.story)}</p>
        <div class="readMore" on:click={open(booster)}>
    			<p>Read more</p>
    		</div>
        <h4 class="author">{booster.name}, {booster.city}</h4>
      </div>

    </div>
  {:else}
    <div class="card strib {booster.type} portrait">
      <h5 class="stamp">{booster.timestamp}</h5>
      <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html booster.story}</p>
        <h4 class="author">{booster.name}, {booster.city}</h4>
      </div>
    </div>
  {/if}


{:else}
  {#if booster.long === "TRUE"}
  <div class="card strib {booster.type} landscape long">
    <h5 class="stamp">{booster.timestamp}</h5>
     <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
    <div class="text">
      <p>{@html shorten(booster.story)}</p>
      <div class="readMore" on:click={open(booster)}>
        <p>Read more</p>
      </div>
      <h4 class="author">{booster.name}, {booster.city}</h4>
    </div>
  </div>
  {:else}
  <div class="card strib {booster.type} landscape">
    <h5 class="stamp">{booster.timestamp}</h5>
     <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
    <div class="text">
      <p>{@html booster.story}</p>
      <h4 class="author">{booster.name}, {booster.city}</h4>
    </div>
  </div>
  {/if}

{/if}
{/if}
