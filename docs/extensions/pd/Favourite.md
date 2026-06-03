---
search:
  boost: 10.0
---

# Class: Favourite 


_Information about favourites_



<div data-search-exclude markdown="1">



URI: [pd:Favourite](https://w3id.org/lmodel/dpv/pd/Favourite)





```mermaid
 classDiagram
    class Favourite
    click Favourite href "../Favourite/"
      Preference <|-- Favourite
        click Preference href "../Preference/"
      

      Favourite <|-- FavouriteColour
        click FavouriteColour href "../FavouriteColour/"
      Favourite <|-- FavouriteFood
        click FavouriteFood href "../FavouriteFood/"
      Favourite <|-- FavouriteMusic
        click FavouriteMusic href "../FavouriteMusic/"
      

      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * **Favourite**
            * [FavouriteColour](FavouriteColour.md)
            * [FavouriteFood](FavouriteFood.md)
            * [FavouriteMusic](FavouriteMusic.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Favourite](https://w3id.org/lmodel/dpv/pd/Favourite) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Favourite




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Favourite |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Favourite |
| native | pd:Favourite |
| exact | dpv_pd:Favourite, dpv_pd_owl:Favourite |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Favourite
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Favourite
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourites
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite
exact_mappings:
- dpv_pd:Favourite
- dpv_pd_owl:Favourite
is_a: Preference
class_uri: pd:Favourite

```
</details>

### Induced

<details>
```yaml
name: Favourite
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Favourite
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourites
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite
exact_mappings:
- dpv_pd:Favourite
- dpv_pd_owl:Favourite
is_a: Preference
class_uri: pd:Favourite

```
</details></div>