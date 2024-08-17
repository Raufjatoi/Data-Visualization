import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_7segment(ax, position, label):
    """Draw a 7-segment display at the given position with label."""
    x_offset, y_offset = position
    segment_positions = {
        'A': [(0.1, 0.8), (0.9, 0.8)],
        'B': [(0.9, 0.8), (0.9, 0.5)],
        'C': [(0.9, 0.3), (0.9, 0.0)],
        'D': [(0.1, 0.0), (0.9, 0.0)],
        'E': [(0.1, 0.3), (0.1, 0.0)],
        'F': [(0.1, 0.8), (0.1, 0.5)],
        'G': [(0.1, 0.4), (0.9, 0.4)],
    }
    
    # Draw segments
    for segment, ((x1, y1), (x2, y2)) in segment_positions.items():
        ax.plot([x1 + x_offset, x2 + x_offset], [y1 + y_offset, y2 + y_offset], 
                color='black', linewidth=5, solid_capstyle='round')
    
    # Label the display
    ax.text(x_offset + 0.5, y_offset - 0.2, label, fontsize=12, ha='center')

def draw_decoder(ax, position):
    """Draw a decoder box at the given position."""
    x, y = position
    ax.add_patch(patches.Rectangle((x, y), 1.5, 1, fill=None, edgecolor='black', linewidth=2))
    ax.text(x + 0.75, y + 0.5, "Decoder", fontsize=12, ha='center', va='center')

def draw_connections(ax, decoder_position, display_positions):
    """Draw connections between the decoder and 7-segment displays."""
    x_dec, y_dec = decoder_position
    for i, (x_disp, y_disp) in enumerate(display_positions):
        for j in range(7):  # 7 segments
            ax.arrow(x_dec + 1.5, y_dec + 0.9 - j*0.1, 
                     x_disp - (x_dec + 1.5), (y_disp + 0.4) - (y_dec + 0.9 - j*0.1),
                     head_width=0.05, head_length=0.1, fc='gray', ec='gray')

def draw_diagram():
    fig, ax = plt.subplots(figsize=(10, 5))
    
    # Draw the decoder
    draw_decoder(ax, (2, 1.5))
    
    # Draw two 7-segment displays
    display_positions = [(5, 3), (7, 3)]
    draw_7segment(ax, display_positions[0], 'Display 1')
    draw_7segment(ax, display_positions[1], 'Display 2')
    
    # Draw connections between the decoder and the displays
    draw_connections(ax, (2, 1.5), display_positions)
    
    # Draw arrows representing inputs to the decoder
    ax.arrow(0.5, 2.3, 1.5, 0, head_width=0.1, head_length=0.2, fc='blue', ec='blue')
    ax.text(0.25, 2.3, "Input 1", fontsize=12, ha='center', va='center')
    ax.arrow(0.5, 1.7, 1.5, 0, head_width=0.1, head_length=0.2, fc='blue', ec='blue')
    ax.text(0.25, 1.7, "Input 2", fontsize=12, ha='center', va='center')
    
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis('off')
    plt.title("System with Two 7-Segment Displays and Decoder")
    plt.show()

draw_diagram()
