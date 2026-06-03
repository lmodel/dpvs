---
search:
  boost: 10.0
---

# Class: HomeLocation 


_Information about a person's home place, including their location,_

_address, and locality_



<div data-search-exclude markdown="1">



URI: [pd:HomeLocation](https://w3id.org/lmodel/dpv/pd/HomeLocation)





```mermaid
 classDiagram
    class HomeLocation
    click HomeLocation href "../HomeLocation/"
      DpvLocation <|-- HomeLocation
        click DpvLocation href "../DpvLocation/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **HomeLocation**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:HomeLocation](https://w3id.org/lmodel/dpv/pd/HomeLocation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Home Place




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#HomeLocation |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:HomeLocation |
| native | pd:HomeLocation |
| exact | dpv_pd:HomeLocation, dpv_pd_owl:HomeLocation |
| close | iso29100:PersonallyIdentifiableInformation |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HomeLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HomeLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about a person''s home place, including their location,

  address, and locality'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Home Place
exact_mappings:
- dpv_pd:HomeLocation
- dpv_pd_owl:HomeLocation
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DpvLocation
class_uri: pd:HomeLocation

```
</details>

### Induced

<details>
```yaml
name: HomeLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HomeLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about a person''s home place, including their location,

  address, and locality'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Home Place
exact_mappings:
- dpv_pd:HomeLocation
- dpv_pd_owl:HomeLocation
close_mappings:
- iso29100:PersonallyIdentifiableInformation
is_a: DpvLocation
class_uri: pd:HomeLocation

```
</details></div>