ComfyUI workflows

# LTX 2.3 Distilled 1 pass. (no upscale, no LLM prompt enhance)
You have to use 25 FPS in this workflow with these models.
Any other FPS causes desync. DO NOT use 24 FPS, this lags the audio behind.
If you use too high of a resolution for a length, you get degraded audio/video outputs and are 100% unusable/worthless.
If you go higher or longer, you will just get a solid black output.


# Ace Step 1.5
The Ace Step 1.5 workflow condenses nodes with subgraphs, to hide stuff you will likely never want to change.
It also adds the option to use an audio file as the latent noise.
It also saves the file with the custom node Yanc which has the date/time format for saving the audio file, but you can delete those 2 if you don't want to use it.
Also added the default node with defeault settings as a disabled node, not connected, for reference.
Lastly, I added a prompt you can copy/paste to an LLM like gemini to make music lyrics/settings.
Also some notes and colored the nodes.
That's all. Nothing else special about this workflow.

# .
.
