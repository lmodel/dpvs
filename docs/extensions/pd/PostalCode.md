---
search:
  boost: 10.0
---

# Class: PostalCode 


_Information about postal code as a location_



<div data-search-exclude markdown="1">



URI: [pd:PostalCode](https://w3id.org/lmodel/dpv/pd/PostalCode)





```mermaid
 classDiagram
    class PostalCode
    click PostalCode href "../PostalCode/"
      DpvLocation <|-- PostalCode
        click DpvLocation href "../DpvLocation/"
      PhysicalAddress <|-- PostalCode
        click PhysicalAddress href "../PhysicalAddress/"
      
      
```





## Inheritance
* [Tracking](Tracking.md)
    * [Contact](Contact.md)
        * [PhysicalAddress](PhysicalAddress.md) [ [DpvLocation](DpvLocation.md)]
            * **PostalCode** [ [DpvLocation](DpvLocation.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:PostalCode](https://w3id.org/lmodel/dpv/pd/PostalCode) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Postal Code




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#PostalCode |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:PostalCode |
| native | pd:PostalCode |
| exact | dpv_pd:PostalCode, dpv_pd_owl:PostalCode |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: PostalCode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PostalCode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about postal code as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Postal Code
exact_mappings:
- dpv_pd:PostalCode
- dpv_pd_owl:PostalCode
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:PostalCode

```
</details>

### Induced

<details>
```yaml
name: PostalCode
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#PostalCode
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about postal code as a location
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Postal Code
exact_mappings:
- dpv_pd:PostalCode
- dpv_pd_owl:PostalCode
is_a: PhysicalAddress
mixins:
- DpvLocation
class_uri: pd:PostalCode

```
</details></div>