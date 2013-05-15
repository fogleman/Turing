#define STAY 0
#define NORTH 1
#define SOUTH 2
#define EAST 3
#define WEST 4

typedef struct {
    int width;      // width of the 2-D tape
    int height;     // height of the 2-D tape
    int states;     // number of states
    int symbols;    // number of symbols
    int position;   // current head position
    int state;      // current state
    int *table;     // transition table (states * symbols * 3)
    int *tape;      // tape memory (width * height)
} Model;

void update(Model *model) {
    // read symbol written on tape at head position
    int symbol = model->tape[model->position];
    // get base index in transition table based on symbol and current state
    int index = (symbol * model->states + model->state) * 3;
    // write new symbol to tape
    model->tape[model->position] = model->table[index];
    // set new state
    model->state = model->table[index + 1];
    // update head position
    int x = model->position % model->width;
    int y = model->position / model->width;
    switch (model->table[index + 2]) {
        case STAY:
            break;
        case NORTH:
            y--;
            y = y < 0 ? model->height - 1 : y;
            break;
        case SOUTH:
            y++;
            y = y < model->height ? y : 0;
            break;
        case EAST:
            x++;
            x = x < model->width ? x : 0;
            break;
        case WEST:
            x--;
            x = x < 0 ? model->width - 1 : x;
            break;
    }
    model->position = y * model->width + x;
}

void updates(Model *model, int count) {
    for (int i = 0; i < count; i++) {
        update(model);
    }
}

void create_image(Model *model, unsigned int *palette, unsigned int *pixels) {
    int size = model->width * model->height;
    for (int i = 0; i < size; i++) {
        pixels[i] = palette[model->tape[i]];
    }
}
