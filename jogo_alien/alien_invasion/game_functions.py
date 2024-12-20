import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, stats,
                     sb, play_button, ship, aliens, bullets):

    """
    Responde a eventos de pressionamento de teclas e de mouse.
    """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings,
                                     screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats,
                              sb, play_button, ship,
                            aliens, bullets, mouse_x, mouse_y)
                
def check_play_button(ai_settings, screen, stats,
                      sb, play_button, ship, aliens,
                          bullets, mouse_x, mouse_y):
    """
    Inicia um novo jogo quando o jogador clicar em Play.
    """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        ai_settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        stats.game_active = True
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    
def update_screen(ai_settings, screen, stats, sb, ship, aliens,
                      bullets, play_button):
    """
    Atualiza as imagens na tela e alterna para a nova tela.
    """
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """
    Responde a pressionamentos de tecla.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        pygame.quit()
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
    """
    Dispara um projétil se o limite ainda não foi alcançado.
    """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_bullet_alien_collisions(ai_settings, screen, stats,
                                      sb, ship,aliens, bullets):
    """
    Responde a colisões entre projéteis e alienígenas.
    """
    collisions = pygame.sprite.groupcollide(bullets, aliens,
                                            True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
        sb.prep_score()
        check_high_score(stats, sb)
        
    if len(aliens) == 0:
    # Destrói os projéteis existentes e cria uma nova frota
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens)

def update_bullets(ai_settings, screen, stats,
                       sb, ship, aliens, bullets):
    """
    Atualiza a posição dos projéteis e se livra dos
    projéteis antigos.
    """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen,stats,
                                  sb, ship, aliens, bullets)


def check_keyup_events(event, ship):
    """
    Responde a solturas de tecla.
    """
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False

def get_number_aliens_x(ai_settings, alien_width):
    """
    Determina o número de alienígenas que cabem em uma linha.
    """
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height*row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    """
    Determina o número de linhas com alienígenas que cabem na tela.
    """
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))

    return number_rows



def create_fleet(ai_settings, screen, ship, aliens):
    """
    Cria uma frota completa de alienígenas.
    """
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    
    number_aliens_x = get_number_aliens_x(ai_settings, alien_width)
    number_rows = get_number_rows(ai_settings,
                              ship.rect.height, alien.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen,
                     aliens, alien_number,row_number)

def change_fleet_direction(ai_settings, aliens):
    """
    Faz toda a frota descer e muda a sua direção.
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed

    ai_settings.fleet_direction *= -1

def check_fleet_edges(ai_settings, aliens):
    """
    Responde apropriadamente se algum alienígena alcançou uma borda.
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
    
def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """
    Atualiza as posições de todos os alienígenas da frota.
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, sb, ship,
                 aliens, bullets)

    check_aliens_bottom(ai_settings, screen, stats,
                        sb, ship, aliens, bullets)

def ship_hit(ai_settings, screen, stats, sb, ship,
                 aliens, bullets):
    """
    Responde ao fato de a espaçonave ter sido atingida
    por um alienígena.
    """
    if stats.ships_left > 0:
        stats.ships_left -= 1
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, screen, stats,
                        sb, ship, aliens, bullets):
    """
    Verifica se algum alienígena alcançou a parte inferior da tela.
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats,
                         sb, ship, aliens, bullets)
            break

def check_high_score(stats, sb):
    """
    Verifica se há uma nova pontuação máxima.
    """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
