import { Vue, Component } from 'nuxt-property-decorator'
import _ from 'lodash'
import { Dictionary, RawLocation, Route } from 'vue-router/types/router'

type QueryParams = Dictionary<string | (string | null)[] | null | undefined>

@Component
export class TaskManagerMixin extends Vue {
  /**
   * Is the given program currently opened
   * @param programId The id which identifies the target program
   */
  protected isActive (programId: string): boolean {
    return this.$route.query[programId] !== undefined
  }

  /**
   * Is the given program currently on top of the window hierarchy
   * @param programId The id which identifies the target program
   */
  protected isOnTop (programId: string): boolean {
    // find the program which is on top
    const top = _.reduce(this.query, (akk, value, key) => {
      const numVal = Number(value)
      if (numVal < akk.index) {
        return { id: key, index: numVal }
      }
      return akk
    }, { id: '', index: Number.MAX_SAFE_INTEGER })

    return top.id === programId
  }

  /**
   * Is the given program currently in a minimized state so that only the header is visible
   * @param programId The id which identifies the target program
   */
  protected isProgramMinimized (programId: string): boolean {
    return this.$route.query[`${programId}_min`] === 'true'
  }

  /**
   * Is the given program currently in a maximized state so that it fills the whole viewport
   * @param programId The id which identifies the target program
   */
  protected isProgramMaximized (programId: string): boolean {
    return this.$route.query[`${programId}_max`] === 'true'
  }

  /**
   * Get the window hierarchy index of the given program
   * @param programId The id which identifies the target program
   */
  protected getProgramIndex (programId: string): number {
    if (!this.isActive(programId)) {
      throw new Error(`program ${programId} is not opened and therefore has no index`)
    }

    return Number(this.query[programId])
  }

  /**
   * Open the given program and place it on top of the window hierarchy
   * @param programIds The IDs which identify the target programs.
   *  The further back the program id is, the further back it will be in the window hierarchy
   */
  protected openProgram (...programIds: string[]): Promise<void | Route> {
    const query = this.lowerAllPrograms(this.query, programIds.length)
    programIds.forEach((programId, index) => {
      query[programId] = String(index + 1)
      delete query[`${programId}_max`]
      delete query[`${programId}_min`]
    })
    return this.navigate({ query })
  }

  /**
   * Close the given program so that it is not displayed anymore
   * @param programId The id which identifies the target program
   */
  protected closeProgram (programId: string): Promise<void | Route> {
    const query: QueryParams = { ...this.$route.query }
    delete query[programId]
    delete query[`${programId}_max`]
    delete query[`${programId}_min`]
    return this.navigate({ query })
  }

  /**
   * Raise an already open program to the top of the window hierarchy
   * @param programId The id which identifies the target program
   */
  protected raiseProgram (programId: string): Promise<void | Route> {
    if (!this.isActive(programId)) {
      throw new Error(`program ${programId} is not opened and therefore cannot be raised`)
    }

    const query = this.lowerAllPrograms(this.query)
    query[programId] = '1'
    return this.navigate({ query })
  }

  /**
   * Minimize an already open program so that only the titlebar is visible
   * @param programId The id which identifies the target program
   */
  protected minimizeProgram (programId: string): Promise<void | Route> {
    const query = this.query
    query[`${programId}_min`] = 'true'
    delete query[`${programId}_max`]
    return this.navigate({ query })
  }

  /**
   * Revert program minimization so that it is displayed normally
   * @param programId The id which identifies the target program
   */
  protected unminimizeProgram (programId: string): Promise<void | Route> {
    const query = this.query
    delete query[`${programId}_min`]
    return this.navigate({ query })
  }

  /**
   * Maximize an already open program so that only the titlebar is visible
   * @param programId The id which identifies the target program
   */
  protected maximizeProgram (programId: string): Promise<void | Route> {
    const query = this.query
    query[`${programId}_max`] = 'true'
    delete query[`${programId}_min`]
    return this.navigate({ query })
  }

  /**
   * Revert program maximization so that it is displayed normally
   * @param programId The id which identifies the target program
   */
  protected unmaximizeProgram (programId: string): Promise<void | Route> {
    const query = this.query
    delete query[`${programId}_max`]
    delete query[`${programId}_min`]
    return this.navigate({ query })
  }

  /**
   * Get the current query parameters but as an object which can safely be passed to `$router.replace({ query })`
   * without raising DuplicateNavigation errors
   */
  private get query (): QueryParams {
    return { ...this.$route.query }
  }

  /**
   * Lower all programs by increasing their respective query parameter by one.
   *
   * This effectively makes room for a new program that can be brought to the top.
   *
   * @param query Existing query parameters in which all programs should be lowered
   * @param by By how much each program should be lowered
   */
  private lowerAllPrograms (query: QueryParams, by: number = 1): QueryParams {
    // @ts-ignore because the type definition for lodash is incorrect here
    return _.mapValues(query, (value: string) => {
      const numVal = Number(value)
      if (Number.isNaN(numVal)) {
        return value
      } else {
        return String(numVal + by)
      }
    })
  }

  /**
   * Execute navigation to new query parameters while ignoring DuplicateNavigation errors
   * @param location Target Location
   */
  private navigate (location: RawLocation): Promise<void | Route> {
    return this.$router.replace(location).catch((reason) => {
      if (reason.name === 'NavigationDuplicated') {
        return
      }
      throw reason
    })
  }
}
