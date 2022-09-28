## API Usage

This documentation provides information on using the Simply Simple Notes API.
With this API, you can create, read, and delete notes.

## Create a note

Adds a note to the notepad.

```bash
$ curl -X POST "127.0.0.1:5000/add" -d '{"message":"my n0te"}'
Note added successfully!
```

## Read a specific note

Reads a note from the notepad by id.

```bash
$ curl -X GET "127.0.0.1:5000/get?id=1"
[(1, 'My Note')]
```

## Read all notes

Reads all notes from the notepad.

```bash
$ curl -X GET "127.0.0.1:5000/get"
[(1, 'My Note'), (2, 'This is a good note')]
```

## Delete a note

Deletes a note from the notepad by id.

```bash
curl -X DELETE "127.0.0.1:5000/delete?id=1"
Note deleted successfully!
```
