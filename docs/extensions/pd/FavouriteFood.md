---
search:
  boost: 10.0
---

# Class: FavouriteFood 


_Information about favourite food_



<div data-search-exclude markdown="1">



URI: [pd:FavouriteFood](https://w3id.org/lmodel/dpv/pd/FavouriteFood)





```mermaid
 classDiagram
    class FavouriteFood
    click FavouriteFood href "../FavouriteFood/"
      Favourite <|-- FavouriteFood
        click Favourite href "../Favourite/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * [Favourite](Favourite.md)
            * **FavouriteFood**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FavouriteFood](https://w3id.org/lmodel/dpv/pd/FavouriteFood) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Favourite Food




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FavouriteFood |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FavouriteFood |
| native | pd:FavouriteFood |
| exact | dpv_pd:FavouriteFood, dpv_pd_owl:FavouriteFood |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FavouriteFood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FavouriteFood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourite food
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite Food
exact_mappings:
- dpv_pd:FavouriteFood
- dpv_pd_owl:FavouriteFood
is_a: Favourite
class_uri: pd:FavouriteFood

```
</details>

### Induced

<details>
```yaml
name: FavouriteFood
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FavouriteFood
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourite food
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite Food
exact_mappings:
- dpv_pd:FavouriteFood
- dpv_pd_owl:FavouriteFood
is_a: Favourite
class_uri: pd:FavouriteFood

```
</details></div>