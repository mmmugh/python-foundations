/* Which volume these harnesses are checking.
 *
 * The fixtures next door -- reference_solutions.py, stdin_answers.py,
 * project_answers.py -- are written against one volume's exercises and key
 * themselves the way that volume's _checks.json does, with no volume in the
 * id. So the volume is named here once, and `qualify()` turns a bare check id
 * into the id the built site uses.
 *
 *     VOLUME=vol2-something node validate_shipped.mjs
 */
import { readFileSync } from "node:fs";

export const REPO = new URL("..", import.meta.url).pathname;
export const VOLUME = process.env.VOLUME || "vol1-foundations";
export const qualify = (id) => `${VOLUME}/${id}`;

export const checks = JSON.parse(
  readFileSync(`${REPO}/volumes/${VOLUME}/content/_checks.json`, "utf8"));

export const boxes = JSON.parse(readFileSync(`${REPO}/site/boxes.json`, "utf8"));
