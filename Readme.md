# Blackbox

Flask-based API mimicking the behavior of six mysterious endpoints provided in a reverse engineering hackathon. Below is a summary of our observations and reverse-engineered logic for each endpoint based on observed I/O behavior.

---

## ✅ Summary of Endpoint Behaviors

### 1. `POST /data`

**Observation:**

* Input: A simple string like `"hi"`
* Output: Base64 encoded string

**Example:**

```json
Input:  { "data": "hi" }
Output: { "result": "aGk=" }
```

**Conclusion:**

* The input string is base64 encoded.

---

### 2. `POST /zap`

**Observation:**

* Input: String with digits and other characters
* Output: All digits removed

**Example:**

```json
Input:  { "data": "hihi123ghjk@/." }
Output: { "result": "hihighjk@/." }
```

**Conclusion:**

* All digits (0–9) are removed, other characters preserved.

---

### 3. `POST /alpha`

**Observation:**

* Input: String with various characters
* Output: `true` if any alphabet character exists; otherwise, `false`

**Example:**

```json
Input:  { "data": "1234!@" }
Output: { "result": false }

Input:  { "data": "hihi123" }
Output: { "result": true }
```

**Conclusion:**

* Detects if any A-Z or a-z character is present.

---

### 4. `POST /fizzbuzz`

**Observation:**

* Any input (numbers, strings, JSON arrays)
* Output: Always returns `false`

**Example:**

```json
Input:  { "data": "[1,2,3]" }
Output: { "result": false }
```

**Conclusion:**

* Function always returns false regardless of input (placeholder/dummy endpoint).

---

### 5. `GET /time`

**Observation:**

* No input required
* Output: A large number that **decreases** with time

**Example:**

```json
Output: { "result": 8148521 }
```

**Conclusion:**

* Returns the number of seconds remaining until a fixed future timestamp (October 6, 2093, 08:16:42 UTC)
* Implemented as: `int(4071760602 - time.time())`

---

### 6. `POST /glitch`

**Observation:**

* Input: Mixed characters (letters, digits, symbols)
* Output: Special characters moved to front; rest reversed

**Example:**

```json
Input:  { "data": "ads12hyQ" }
Output: { "result": "Qyh21sda" }
```

**Conclusion:**

* All non-alphanumeric characters are extracted and prepended
* Remaining characters (letters + digits) are reversed
* Final output = specials + reversed alphanumerics

---

## 🧪 Overall Testing Strategy

* Used trial and error with various data types: strings, digits, arrays, symbols
* Compared known encodings (e.g., base64), and output lengths
* Analyzed patterns across outputs to deduce static or computed behavior

---

## 📁 Files in the Repository

* `main.py` - Main Flask backend implementation
* `README.md` - This summary of behavior and observations

