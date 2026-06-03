---
search:
  boost: 10.0
---

# Class: FavouriteMusic 


_Information about favourite music_



<div data-search-exclude markdown="1">



URI: [pd:FavouriteMusic](https://w3id.org/lmodel/dpv/pd/FavouriteMusic)





```mermaid
 classDiagram
    class FavouriteMusic
    click FavouriteMusic href "../FavouriteMusic/"
      Favourite <|-- FavouriteMusic
        click Favourite href "../Favourite/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * [Favourite](Favourite.md)
            * **FavouriteMusic**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FavouriteMusic](https://w3id.org/lmodel/dpv/pd/FavouriteMusic) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Favourite Music




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FavouriteMusic |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FavouriteMusic |
| native | pd:FavouriteMusic |
| exact | dpv_pd:FavouriteMusic, dpv_pd_owl:FavouriteMusic |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FavouriteMusic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FavouriteMusic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourite music
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite Music
exact_mappings:
- dpv_pd:FavouriteMusic
- dpv_pd_owl:FavouriteMusic
is_a: Favourite
class_uri: pd:FavouriteMusic

```
</details>

### Induced

<details>
```yaml
name: FavouriteMusic
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FavouriteMusic
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourite music
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite Music
exact_mappings:
- dpv_pd:FavouriteMusic
- dpv_pd_owl:FavouriteMusic
is_a: Favourite
class_uri: pd:FavouriteMusic

```
</details></div>