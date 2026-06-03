---
search:
  boost: 10.0
---

# Class: Connection 


_Information about and including connections in a social network_



<div data-search-exclude markdown="1">



URI: [pd:Connection](https://w3id.org/lmodel/dpv/pd/Connection)





```mermaid
 classDiagram
    class Connection
    click Connection href "../Connection/"
      SocialNetwork <|-- Connection
        click SocialNetwork href "../SocialNetwork/"
      
      
```





## Inheritance
* [Social](Social.md)
    * [SocialNetwork](SocialNetwork.md)
        * **Connection**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Connection](https://w3id.org/lmodel/dpv/pd/Connection) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Connection




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Connection |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Connection |
| native | pd:Connection |
| exact | dpv_pd:Connection, dpv_pd_owl:Connection |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Connection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Connection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about and including connections in a social network
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Connection
exact_mappings:
- dpv_pd:Connection
- dpv_pd_owl:Connection
is_a: SocialNetwork
class_uri: pd:Connection

```
</details>

### Induced

<details>
```yaml
name: Connection
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Connection
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about and including connections in a social network
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Connection
exact_mappings:
- dpv_pd:Connection
- dpv_pd_owl:Connection
is_a: SocialNetwork
class_uri: pd:Connection

```
</details></div>