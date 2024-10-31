# Chemins vers les répertoires
SRC_DIR = src
OBJ_DIR = obj
BIN_DIR = bin
EXEC = $(BIN_DIR)/hello
OBJ = $(OBJ_DIR)/hello.o
all: $(EXEC)

$(EXEC): $(OBJ)
	@mkdir -p $(BIN_DIR)
	ld -m elf_i386 -o $(EXEC) $(OBJ)

$(OBJ): $(SRC_DIR)/hello.asm
	@mkdir -p $(OBJ_DIR)
	nasm -f elf32 -o $(OBJ) $(SRC_DIR)/hello.asm

clean:
	rm -rf $(OBJ_DIR) $(BIN_DIR)

rebuild: clean all
