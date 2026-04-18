# Event System Prototype

**Status:** ✓ Implemented  
**Date:** 2026-04-18  
**Purpose:** Validate event-driven architecture with local Ollama before building GTK4 UI

## What's Built

This prototype implements the core event system from Phase 2:

- `EventBus` - Pub/sub event routing
- `EventEmitter` - Event detection and emission  
- `OllamaClient` - LLM client with event integration
- `prototype_cli.py` - CLI demo that ties it all together

## Running the Prototype

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Make sure Ollama is running:**
   ```bash
   ollama serve
   ```

3. **Run the prototype:**
   ```bash
   python prototype_cli.py
   ```

## What It Demonstrates

- ✓ Event bus routes events to subscribers
- ✓ Events emit on LLM success/failure
- ✓ Multiple handlers can subscribe to same event
- ✓ Failures don't crash the event loop
- ✓ Session lifecycle tracked (start/end)

## Sample Output

```
============================================================
Native Claude Client - Event System Prototype
============================================================

Checking Ollama connection...
✓ Found 3 model(s): llama3.2, mistral, codellama

--- Starting Test Session ---
✓ Session started: a1b2c3d4... (domain: prototype)

Test 1: Normal chat call
✓ Tool succeeded: ollama:llama3.2
  Response: "Hello, how are you today?"

Test 2: Intentional failure (non-existent model)
✗ Tool failed: ollama:nonexistent-model-xyz (api_error)
  Expected error: Ollama API error: HTTP 404

Test 3: Rapid fire calls (3x)
✓ Tool succeeded: ollama:llama3.2
  Call 1: Success (15 chars)
✓ Tool succeeded: ollama:llama3.2
  Call 2: Success (18 chars)
✓ Tool succeeded: ollama:llama3.2
  Call 3: Success (22 chars)

--- Ending Test Session ---
✓ Session ended: 2.3s

Total events emitted: 11
============================================================
Event system validated ✓
Next step: Add FailureTracker to monitor consecutive failures
============================================================
```

## Testing

Run unit tests:
```bash
pytest tests/
```

## Next Steps

1. **Add FailureTracker** - Monitor consecutive failures and emit threshold events
2. **Add TokenMonitor** - Track token usage percentages (when we add Claude client)
3. **Add HookExecutor** - Load hooks and execute on events
4. **Build GTK4 UI** - Wrap this event system in a native interface

## Why This Approach?

Testing the brains (event system) with cheap local models before building the UI:
- Validates architecture cheaply
- Tests failure patterns with models we can intentionally break
- Debugs event flow without burning Claude credits
- Proves the design works before GTK4 investment

---

**Built:** 2026-04-18  
**By:** Vector (with Uncle Tallest)
