/**
 * Audioworklet Registry for Félix
 * Manages worklet creation and registration
 */

/**
 * Registry to map attached worklets by their audio-context
 * Any module using `audioContext.audioWorklet.addModule()` should register here
 */
export const registeredWorklets = new Map();

/**
 * Create a worklet URL from source code
 * @param {string} workletName - Name to register the processor as
 * @param {string} workletSrc - Source code of the worklet processor
 * @returns {string} Object URL for the worklet
 */
export const createWorkletFromSrc = (workletName, workletSrc) => {
  const script = new Blob(
    [`registerProcessor("${workletName}", ${workletSrc})`],
    {
      type: 'application/javascript',
    }
  );

  return URL.createObjectURL(script);
};

/**
 * Load a worklet from a file path
 * @param {string} workletPath - Path to the worklet file
 * @returns {string} URL for the worklet module
 */
export const loadWorkletFromPath = (workletPath) => {
  // For file-based worklets, return the path directly
  // The AudioWorklet API will handle loading
  return new URL(workletPath, import.meta.url).href;
};

/**
 * Register a worklet with its handlers
 * @param {AudioContext} context - The audio context
 * @param {string} workletName - Name of the worklet
 * @param {AudioWorkletNode} node - The worklet node
 * @param {Array<Function>} handlers - Message handlers for the worklet
 */
export const registerWorklet = (context, workletName, node, handlers = []) => {
  let workletsRecord = registeredWorklets.get(context);
  
  if (!workletsRecord) {
    registeredWorklets.set(context, {});
    workletsRecord = registeredWorklets.get(context);
  }
  
  workletsRecord[workletName] = {
    node,
    handlers
  };
};

/**
 * Get registered worklet for a context
 * @param {AudioContext} context - The audio context
 * @param {string} workletName - Name of the worklet
 * @returns {Object|null} Worklet record or null if not found
 */
export const getWorklet = (context, workletName) => {
  const workletsRecord = registeredWorklets.get(context);
  return workletsRecord ? workletsRecord[workletName] : null;
};

/**
 * Clean up worklets for a context
 * @param {AudioContext} context - The audio context to clean up
 */
export const cleanupWorklets = (context) => {
  const workletsRecord = registeredWorklets.get(context);
  
  if (workletsRecord) {
    Object.values(workletsRecord).forEach(({ node }) => {
      if (node) {
        node.port.close();
        node.disconnect();
      }
    });
    
    registeredWorklets.delete(context);
  }
};
