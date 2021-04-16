const express = require("express");
const Queue = require("bull");
const db = require("./db.js");
const QueryStream = require("pg-query-stream");
const JSONStream = require("JSONStream");
const es = require("event-stream");

// Serve on PORT on Heroku and on localhost:5000 locally
const PORT = process.env.PORT || "5000";
// Connect to a local redis intance locally, and the Heroku-provided URL in production
const REDIS_URL = process.env.REDIS_URL || "redis://127.0.0.1:6379";

const app = express();

// Create / Connect to a named work queue
// const activistsQueue = new Queue("activists", REDIS_URL);
const typeQueueActivists = new Queue("activists", REDIS_URL);
const typeQueueActivistPressures = new Queue("activist_pressures", REDIS_URL);
const typeQueueFormEntries = new Queue("form_entries", REDIS_URL);
const typeQueueDonations = new Queue("donations", REDIS_URL);

const typeQueue = (type) => {
  switch (type) {
    case "activists":
      return typeQueueActivists;
    case "activist_pressures":
      return typeQueueActivistPressures;
    case "form_entries":
      return typeQueueFormEntries;
    case "donations":
      return typeQueueDonations;
    default:
      break;
  }
};

// Serve the two static assets
app.get("/", (req, res) => res.sendFile("index.html", { root: __dirname }));
app.get("/client.js", (req, res) =>
  res.sendFile("client.js", { root: __dirname })
);

// Kick off a new job by adding it to the work queue
app.post("/job", async (req, res) => {
  // This would be where you could pass arguments to the job
  // Ex: workQueue.add({ url: 'https://www.heroku.com' })
  // Docs: https://github.com/OptimalBits/bull/blob/develop/REFERENCE.md#queueadd
  let job = await typeQueueActivists.add();
  res.json({ id: job.id });
});

const writableStream = new Stream.Writable();

writableStream._write = (chunk, encoding, next) => {
  console.log(chunk.toString());
  // let job = await workQueue.add(chunk.toString());
  next();
};

// Allows the client to query the state of a background job
app.get("/activists/:community_id", async (req, res) => {
  const client = await db.getClient();
  // let community_id = req.params.community_id;
  // const query = new QueryStream(
  //   "SELECT a.* FROM activists a where a.community_id = $1",
  //   [community_id]
  // );
  const query = new QueryStream("SELECT a.* FROM activists a");
  const stream = client.query(query);
  //release the client when the stream is finished
  stream.on("end", () => console.log("terminou..."));

  stream.pipe(JSONStream.stringify()).pipe(res);
  // res.json({});
});

// You can listen to global events to get notified when jobs are processed
typeQueue("activists").on("global:completed", (jobId, result) => {
  console.log(`Activists Job completed ${result}`);
});
typeQueue("form_entries").on("global:completed", (jobId, result) => {
  console.log(`Actions Job completed ${result}`);
});
typeQueue("donations").on("global:completed", (jobId, result) => {
  console.log(`Actions Job completed ${result}`);
});
typeQueue("activist_pressures").on("global:completed", (jobId, result) => {
  console.log(`Actions Job completed ${result}`);
});

app.listen(PORT, () => console.log("Server started!"));
