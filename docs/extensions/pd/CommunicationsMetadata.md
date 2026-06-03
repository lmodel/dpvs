---
search:
  boost: 10.0
---

# Class: CommunicationsMetadata 


_Information about communication metadata in the public sphere_



<div data-search-exclude markdown="1">



URI: [pd:CommunicationsMetadata](https://w3id.org/lmodel/dpv/pd/CommunicationsMetadata)





```mermaid
 classDiagram
    class CommunicationsMetadata
    click CommunicationsMetadata href "../CommunicationsMetadata/"
      PublicLife <|-- CommunicationsMetadata
        click PublicLife href "../PublicLife/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [PublicLife](PublicLife.md)
        * **CommunicationsMetadata**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:CommunicationsMetadata](https://w3id.org/lmodel/dpv/pd/CommunicationsMetadata) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Communications Metadata




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#CommunicationsMetadata |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:CommunicationsMetadata |
| native | pd:CommunicationsMetadata |
| exact | dpv_pd:CommunicationsMetadata, dpv_pd_owl:CommunicationsMetadata |
| related | svd:Interactive |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CommunicationsMetadata
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CommunicationsMetadata
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about communication metadata in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Communications Metadata
exact_mappings:
- dpv_pd:CommunicationsMetadata
- dpv_pd_owl:CommunicationsMetadata
related_mappings:
- svd:Interactive
is_a: PublicLife
class_uri: pd:CommunicationsMetadata

```
</details>

### Induced

<details>
```yaml
name: CommunicationsMetadata
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#CommunicationsMetadata
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about communication metadata in the public sphere
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Communications Metadata
exact_mappings:
- dpv_pd:CommunicationsMetadata
- dpv_pd_owl:CommunicationsMetadata
related_mappings:
- svd:Interactive
is_a: PublicLife
class_uri: pd:CommunicationsMetadata

```
</details></div>