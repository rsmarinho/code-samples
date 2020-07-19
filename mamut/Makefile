TARGET = mamut

CC = gcc
CFLAGS = -std=c99 -Wall -I. -I./src

LINKER = gcc
LFLAGS = -Wall -I. -lm

SRCDIR = src
OBJDIR = obj

SOURCES := $(wildcard $(SRCDIR)/*.c)
INCLUDES := $(wildcard $(SRCDIR)/*.h)
OBJECTS := $(SOURCES:$(SRCDIR)/%.c=$(OBJDIR)/%.o)
rm = rm -rf

all: dir $(TARGET)
	
dir:
	@mkdir $(OBJDIR)
	@echo "Creating Directories"

$(TARGET): $(OBJECTS)
	@$(LINKER) $(OBJECTS) $(LFLAGS) -o $@
	@echo "Linking complete!"

$(OBJECTS): $(OBJDIR)/%.o : $(SRCDIR)/%.c
	@$(CC) $(CFLAGS) -c $< -o $@
	@echo "Compiled "$<" successfully!"

.PHONY: clean
clean:
	@$(rm) $(OBJDIR)
	@echo "Cleanup complete!"

.PHONY: remove
remove: clean
	@$(rm) $(TARGET)
	@echo "Executable removed!"
