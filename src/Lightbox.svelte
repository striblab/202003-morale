<script>
  import { onMount, onDestroy } from 'svelte';

  export let lightbox_booster;
  export let store;

  let pWidth = 600;
  let pHeight = 1000;

  let lWidth = 1000;
  let lHeight = 600;

  let pUrl = lightbox_booster.asset + '?w=' + pWidth + '&h=' + pHeight + '&fit=crop&crop=faces&max-h=900' + '&cache=trash';
  let lUrl = lightbox_booster.asset + '?w=' + lWidth + '&h=' + lHeight + '&fit=crop&crop=faces&max-h=600' + '&cache=trash';

  let w = 300;
  let h = 400;

  const unsubscribe = store.subscribe(value => {
		lightbox_booster = value;
	});

	onDestroy(unsubscribe);
</script>



{#if lightbox_booster.type === "video"}

{#if lightbox_booster.from_strib === "TRUE"}

  {#if lightbox_booster.shape === "Portrait"}

    {#if lightbox_booster.long === "TRUE"}

      <div class="card strib {lightbox_booster.type} portrait long">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
        <video height="400" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
          <source src="{lightbox_booster.asset}" type="video/quicktime">
        </video>
        <div class="text">
          <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
        </div>
      </div>

    {:else}

      <div class="card strib {lightbox_booster.type} portrait">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
        <video height="400" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
          <source src="{lightbox_booster.asset}" type="video/quicktime">
        </video>
        <div class="text">
          <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
        </div>
      </div>

    {/if}

  {:else}

    {#if lightbox_booster.long === "TRUE"}
      <div class="card strib {lightbox_booster.type} landscape long">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>

        <video height="300" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
        </video>
        <div class="text">
           <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
        </div>

      </div>
    {:else}
    <div class="card strib {lightbox_booster.type} landscape">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>

        <video height="300" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
        </video>
        <div class="text">
           <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
        </div>

      </div>
    {/if}

  {/if}

{:else}

  {#if lightbox_booster.shape === "Portrait"}

    {#if lightbox_booster.long === "TRUE"}

      <div class="card strib {lightbox_booster.type} portrait long">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
        <video height="400" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
          <source src="{lightbox_booster.asset}" type="video/quicktime">
        </video>
        <div class="text">
          <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
        </div>
      </div>

    {:else}

      <div class="card strib {lightbox_booster.type} portrait">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
        <video height="400" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
          <source src="{lightbox_booster.asset}" type="video/quicktime">
        </video>
        <div class="text">
          <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
        </div>
      </div>

    {/if}

  {:else}

    {#if lightbox_booster.long === "TRUE"}
      <div class="card strib {lightbox_booster.type} landscape long">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>

        <video height="300" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
        </video>
        <div class="text">
           <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
        </div>

      </div>
    {:else}
    <div class="card strib {lightbox_booster.type} landscape">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>

        <video height="300" src="{lightbox_booster.asset}" controls>
          <source src="{lightbox_booster.asset}" type="video/mp4">
        </video>
        <div class="text">
           <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
        </div>

      </div>
    {/if}

  {/if}

{/if}

{:else if lightbox_booster.type === "photo"}

  {#if lightbox_booster.from_strib === "TRUE"}

    {#if lightbox_booster.shape === "Portrait"}

      {#if lightbox_booster.long === "TRUE"}
        <div class="card strib {lightbox_booster.type} portrait long">
          <h5 class="stamp">{lightbox_booster.timestamp}</h5>
          <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
          <div class="text">
            <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
            <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
          </div>
        </div>
      {:else}
        <div class="card strib {lightbox_booster.type} portrait">
          <h5 class="stamp">{lightbox_booster.timestamp}</h5>
          <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
          <div class="text">
            <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
            <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
          </div>
        </div>
      {/if}


    {:else}
      {#if lightbox_booster.long === "TRUE"}
      <div class="card strib {lightbox_booster.type} landscape long">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
         <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
        <div class="text">
          <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
        </div>
      </div>
      {:else}
      <div class="card strib {lightbox_booster.type} landscape">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
         <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
        <div class="text">
          <p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
        </div>
      </div>
      {/if}


    {/if}

  {:else}

  {#if lightbox_booster.shape === "Portrait"}

    {#if lightbox_booster.long === "TRUE"}
      <div class="card strib {lightbox_booster.type} portrait long">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
        <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
        <div class="text">
          <p>{@html lightbox_booster.story}</p>
          <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
        </div>
      </div>
    {:else}
      <div class="card strib {lightbox_booster.type} portrait">
        <h5 class="stamp">{lightbox_booster.timestamp}</h5>
        <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({pUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
        <div class="text">
          <p>{@html lightbox_booster.story}</p>
          <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
        </div>
      </div>
    {/if}


  {:else}
    {#if lightbox_booster.long === "TRUE"}
    <div class="card strib {lightbox_booster.type} landscape long">
      <h5 class="stamp">{lightbox_booster.timestamp}</h5>
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html lightbox_booster.story}</p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
      </div>
    </div>
    {:else}
    <div class="card strib {lightbox_booster.type} landscape">
      <h5 class="stamp">{lightbox_booster.timestamp}</h5>
       <div class="photograph" style="background-color:#efefef;width:100%;background-image:url({lUrl});background-repeat:no-repeat;background-size:100%;background-position:center center;"></div>
      <div class="text">
        <p>{@html lightbox_booster.story}</p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
      </div>
    </div>
    {/if}

  {/if}

  {/if}

{:else if lightbox_booster.type === "text"}

  {#if lightbox_booster.from_strib === "TRUE"}

  {#if lightbox_booster.long === "TRUE"}

  <div class="card strib {lightbox_booster.type} long">
  	<div class="text">
  		<h5 class="stamp">{lightbox_booster.timestamp} • <span class="green">Star Tribune</span></h5>
  		<p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
  	</div>
  </div>

  {:else}

  <div class="card strib {lightbox_booster.type}">
  	<div class="text">
  		<h5 class="stamp">{lightbox_booster.timestamp} • <span class="green">Star Tribune</span></h5>
  		<p>{@html lightbox_booster.story} <a href="{lightbox_booster.url}" target="_blank">Read more</a></p>
          <h4 class="author">{lightbox_booster.name}, Star Tribune</h4>
  	</div>
  </div>

  {/if}

  {:else}

  {#if lightbox_booster.long === "TRUE"}

  <div class="card {lightbox_booster.type} long">
  	<div class="text">
  		<h5 class="stamp">{lightbox_booster.timestamp}</h5>
  			<p>{@html lightbox_booster.story}</p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
  	</div>
  </div>

  {:else}

  <div class="card {lightbox_booster.type}">
  	<div class="text">
  		<h5 class="stamp">{lightbox_booster.timestamp}</h5>
  			<p>{@html lightbox_booster.story}</p>
        <h4 class="author">{lightbox_booster.name}, {lightbox_booster.city}</h4>
  	</div>
  </div>

  {/if}

  {/if}

{/if}
