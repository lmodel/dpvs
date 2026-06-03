---
search:
  boost: 10.0
---

# Class: FavouriteColour 


_Information about favourite colour_



<div data-search-exclude markdown="1">



URI: [pd:FavouriteColour](https://w3id.org/lmodel/dpv/pd/FavouriteColour)





```mermaid
 classDiagram
    class FavouriteColour
    click FavouriteColour href "../FavouriteColour/"
      Favourite <|-- FavouriteColour
        click Favourite href "../Favourite/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * [Favourite](Favourite.md)
            * **FavouriteColour**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:FavouriteColour](https://w3id.org/lmodel/dpv/pd/FavouriteColour) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Favourite Colour




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#FavouriteColour |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:FavouriteColour |
| native | pd:FavouriteColour |
| exact | dpv_pd:FavouriteColour, dpv_pd_owl:FavouriteColour |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: FavouriteColour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FavouriteColour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourite colour
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite Colour
exact_mappings:
- dpv_pd:FavouriteColour
- dpv_pd_owl:FavouriteColour
is_a: Favourite
class_uri: pd:FavouriteColour

```
</details>

### Induced

<details>
```yaml
name: FavouriteColour
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#FavouriteColour
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about favourite colour
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Favourite Colour
exact_mappings:
- dpv_pd:FavouriteColour
- dpv_pd_owl:FavouriteColour
is_a: Favourite
class_uri: pd:FavouriteColour

```
</details></div>