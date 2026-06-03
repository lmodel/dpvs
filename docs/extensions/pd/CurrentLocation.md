---
search:
  boost: 10.0
---

# Class: CurrentLocation 


_Information about a person's current location (e.g. by asking the_

_address, using GPS)_



<div data-search-exclude markdown="1">



URI: [pd:CurrentLocation](https://w3id.org/lmodel/dpv/pd/CurrentLocation)





```mermaid
 classDiagram
    class CurrentLocation
    click CurrentLocation href "../CurrentLocation/"
      DpvLocation <|-- CurrentLocation
        click DpvLocation href "../DpvLocation/"
      

      CurrentLocation <|-- GPSCoordinate
        click GPSCoordinate href "../GPSCoordinate/"
      

      
```





## Inheritance
* [Tracking](Tracking.md)
    * [DpvLocation](DpvLocation.md)
        * **CurrentLocation**
            * [GPSCoordinate](GPSCoordinate.md) [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CurrentLocation](https://w3id.org/lmodel/dpv/pd/CurrentLocation) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Current Location




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CurrentLocation |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CurrentLocation |
| native | pd:CurrentLocation |
| exact | dpv_pd:CurrentLocation, dpv_pd_owl:CurrentLocation |
| related | iso29100:PIIProcessingActivity |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CurrentLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CurrentLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about a person''s current location (e.g. by asking the

  address, using GPS)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Current Location
exact_mappings:
- dpv_pd:CurrentLocation
- dpv_pd_owl:CurrentLocation
related_mappings:
- iso29100:PIIProcessingActivity
is_a: DpvLocation
class_uri: pd:CurrentLocation

```
</details>

### Induced

<details>
```yaml
name: CurrentLocation
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CurrentLocation
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about a person''s current location (e.g. by asking the

  address, using GPS)'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Current Location
exact_mappings:
- dpv_pd:CurrentLocation
- dpv_pd_owl:CurrentLocation
related_mappings:
- iso29100:PIIProcessingActivity
is_a: DpvLocation
class_uri: pd:CurrentLocation

```
</details></div>