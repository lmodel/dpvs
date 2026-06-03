---
search:
  boost: 10.0
---

# Class: Locality 


_Information about locality e.g. city, village, town, portion of a city_

_as a location_



<div data-search-exclude markdown="1">



URI: [pd:Locality](https://w3id.org/lmodel/dpv/pd/Locality)





```mermaid
 classDiagram
    class Locality
    click Locality href "../Locality/"
      DpvLocation <|-- Locality
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- Locality
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **Locality** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Locality](https://w3id.org/lmodel/dpv/pd/Locality) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Locality




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Locality |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Locality |
| native | pd:Locality |
| exact | dpv_pd:Locality, dpv_pd_owl:Locality |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Locality
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Locality
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about locality e.g. city, village, town, portion of a city

  as a location'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Locality
exact_mappings:
- dpv_pd:Locality
- dpv_pd_owl:Locality
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:Locality

```
</details>

### Induced

<details>
```yaml
name: Locality
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Locality
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about locality e.g. city, village, town, portion of a city

  as a location'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Locality
exact_mappings:
- dpv_pd:Locality
- dpv_pd_owl:Locality
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:Locality

```
</details></div>